"""Extract text from a tax-authority PDF using only the standard library.

Written for the annual update runbook. Revenue departments publish rate
schedules, form instructions and administrative rules as PDFs, and the usual
Python readers are not always available — this environment's `pypdf` and
`cryptography` both fail on a broken `_cffi_backend`. This module needs
neither.

Handles:
  * FlateDecode streams and compressed object streams (PDF 1.5+)
  * AES-256 encrypted files with an empty user password (revision 5/6), which
    is how several states ship their forms; decryption uses the pure-Python
    AES in `pdf_aes.py`
  * simple and 2-byte CID fonts via /ToUnicode CMaps
  * literal and hex show operators
  * Tm/Td/TD/T*/TL text-matrix tracking, so lines come out in reading order

Usage:
    python3 scripts/read-tax-pdf.py FILE.pdf [COLUMNS] [PAGE_WIDTH]

COLUMNS splits each page into that many vertical bands and emits them in
order, which is what makes a two- or three-column instruction booklet
readable. Default 1. PAGE_WIDTH defaults to 612 (US Letter); pass 595 for A4.

A caution learned the hard way: text extracted from a multi-column layout can
interleave two unrelated columns into one plausible-looking sentence. Always
read enough surrounding lines to see the column boundaries before quoting a
figure from the output.
"""
import re, sys, zlib

path = sys.argv[1]
NCOL = int(sys.argv[2]) if len(sys.argv) > 2 else 1
PW   = float(sys.argv[3]) if len(sys.argv) > 3 else 612.0
data = open(path, 'rb').read()


# ---- standard security handler, empty user password (R6/AES-256 and R<=4/RC4) ----
FILE_KEY = None
_ENC_R = None
def _find_enc_dict(buf):
    m = re.search(rb'/Filter\s*/Standard(.{0,2000}?)>>', buf, re.S)
    return m.group(0) if m else None

def _pdfstr(blob, key):
    # walk the literal string honouring escapes and nested parens; a lookahead
    # regex truncates whenever the random bytes happen to contain ")/"
    m = re.search(key + rb'\s*\(', blob)
    if m:
        i, depth, out = m.end(), 1, bytearray()
        while i < len(blob):
            c = blob[i]
            if c == 0x5C:                      # backslash
                nxt = blob[i+1:i+2]
                oct_ = re.match(rb'[0-7]{1,3}', blob[i+1:i+4])
                if oct_:
                    out.append(int(oct_.group(0), 8) & 0xFF); i += 1 + len(oct_.group(0))
                else:
                    out += {b'n': b'\n', b'r': b'\r', b't': b'\t', b'b': b'\b',
                            b'f': b'\f'}.get(nxt, nxt)
                    i += 2
                continue
            if c == 0x28: depth += 1
            elif c == 0x29:
                depth -= 1
                if depth == 0: return bytes(out)
            out.append(c); i += 1
        return bytes(out)
    m = re.search(key + rb'\s*<([0-9A-Fa-f\s]*)>', blob, re.S)
    if m:
        return bytes.fromhex(re.sub(rb'\s', b'', m.group(1)).decode())
    return None

_encblob = _find_enc_dict(data)
if _encblob:
    import hashlib
    import os as _os
    _sd = _os.path.dirname(_os.path.abspath(__file__))
    if _sd not in sys.path: sys.path.insert(0, _sd)
    try:
        import pdf_aes as _aes
    except Exception:
        _aes = None
    mR = re.search(rb'/R\s+(\d+)', _encblob)
    _ENC_R = int(mR.group(1)) if mR else None
    U = _pdfstr(_encblob, rb'/U'); UE = _pdfstr(_encblob, rb'/UE')
    if _ENC_R in (5, 6) and U and UE and _aes:
        def _hash2b(pw, salt, udata):
            K = hashlib.sha256(pw + salt + udata).digest()
            if _ENC_R == 5:
                return K
            i = 0
            while True:
                K1 = (pw + K + udata) * 64
                E = _aes.cbc_encrypt(K[:16], K[16:32], K1)
                mod = sum(E[:16]) % 3
                K = (hashlib.sha256 if mod == 0 else hashlib.sha384 if mod == 1 else hashlib.sha512)(E).digest()
                i += 1
                if i >= 64 and E[-1] <= i - 32:
                    return K[:32]
        ik = _hash2b(b'', U[40:48], b'')
        FILE_KEY = _aes.cbc_decrypt(ik, b'\x00' * 16, UE)

        def _decrypt(raw, num):
            if len(raw) <= 16: return raw
            out = _aes.cbc_decrypt(FILE_KEY, raw[:16], raw[16:])
            return out[:-out[-1]] if out and 1 <= out[-1] <= 16 else out
    else:
        def _decrypt(raw, num): return raw
else:
    def _decrypt(raw, num): return raw

objs = {}
for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b', data):
    e = data.find(b'endobj', m.end())
    objs[int(m.group(1))] = data[m.end():e if e > 0 else len(data)]

def stream_of(n):
    b = objs.get(n, b'')
    m = re.search(rb'stream\r?\n', b)
    if not m: return b''
    raw = b[m.end():b.find(b'endstream', m.end())]
    if FILE_KEY is not None and not re.search(rb'/Type\s*/XRef', b):
        raw = _decrypt(raw, n)
    try: return zlib.decompress(raw)
    except Exception: return raw

# expand compressed object streams (PDF 1.5+), whose contents the top-level
# "N 0 obj" scan cannot see
for _n in [k for k, v in list(objs.items()) if re.search(rb'/Type\s*/ObjStm', v)]:
    body = objs[_n]
    data_ = stream_of(_n)
    mN = re.search(rb'/N\s+(\d+)', body)
    mF = re.search(rb'/First\s+(\d+)', body)
    if not (mN and mF and data_): continue
    N, first = int(mN.group(1)), int(mF.group(1))
    nums = re.findall(rb'(\d+)\s+(\d+)', data_[:first])[:N]
    for i, (num, off) in enumerate(nums):
        start = first + int(off)
        end = first + int(nums[i+1][1]) if i + 1 < len(nums) else len(data_)
        objs.setdefault(int(num), data_[start:end])

def parse_cmap(b):
    mp, nb = {}, 1
    t = b.decode('latin-1', 'replace')
    cs = re.search(r'begincodespacerange(.*?)endcodespacerange', t, re.S)
    if cs:
        h = re.search(r'<([0-9A-Fa-f]+)>', cs.group(1))
        if h: nb = max(1, len(h.group(1)) // 2)
    for blk in re.findall(r'beginbfchar(.*?)endbfchar', t, re.S):
        for s, d in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            mp[int(s, 16)] = ''.join(chr(int(d[i:i+4], 16)) for i in range(0, len(d), 4))
    for blk in re.findall(r'beginbfrange(.*?)endbfrange', t, re.S):
        for lo, hi, d in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            base = int(d, 16)
            for i, c in enumerate(range(int(lo, 16), int(hi, 16) + 1)):
                mp[c] = chr(base + i)
    return mp, nb

font = {n: parse_cmap(stream_of(int(m.group(1))))
        for n, b in objs.items() if (m := re.search(rb'/ToUnicode\s+(\d+)\s+0\s+R', b))}

def res_map(body):
    out = {}
    m = re.search(rb'/Font\s*<<(.*?)>>', body, re.S)
    blob = m.group(1) if m else (objs.get(int(m2.group(1)), b'')
                                 if (m2 := re.search(rb'/Font\s+(\d+)\s+0\s+R', body)) else None)
    if blob:
        for name, onum in re.findall(rb'/([\w.]+)\s+(\d+)\s+0\s+R', blob):
            out[name.decode()] = font.get(int(onum), ({}, 1))
    return out

pages = []
for n, b in objs.items():
    if re.search(rb'/Type\s*/Page\b', b):
        cm = re.search(rb'/Contents\s+(\d+)\s+0\s+R', b)
        rm = re.search(rb'/Resources\s+(\d+)\s+0\s+R', b)
        if cm:
            pages.append((n, int(cm.group(1)),
                          res_map(objs.get(int(rm.group(1)), b'')) if rm else res_map(b)))
pages.sort()

N = r'[-+]?[\d.]+'
TOK = re.compile((
    r'/([\w.]+)\s+' + N + r'\s+Tf'
    r'|(' + N + r')\s+(' + N + r')\s+(Td|TD)'
    r'|(' + N + r')\s+(' + N + r')\s+(' + N + r')\s+(' + N + r')\s+(' + N + r')\s+(' + N + r')\s+Tm'
    r'|(' + N + r')\s+TL|\bT\*|\bBT\b'
    r'|\[((?:\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f]*>|[^\[\]])*)\]\s*TJ'
    r'|(<[0-9A-Fa-f]*>|\((?:\\.|[^\\()])*\))\s*(?:Tj|\')').encode(), re.S)

def unesc(b):
    b = re.sub(rb'\\([0-7]{1,3})', lambda m: bytes([int(m.group(1), 8) & 0xFF]), b)
    return re.sub(rb'\\(.)', rb'\1', b)

def show(tok, cmap, nb):
    parts = []
    for p in re.findall(rb'<([0-9A-Fa-f]*)>|\(((?:\\.|[^\\()])*)\)', tok):
        if p[0]:
            h = p[0].decode(); w = nb * 2
            parts.append(''.join(
                cmap.get(int(h[i:i+w], 16), chr(int(h[i:i+w], 16)) if (not cmap and w == 2) else '')
                for i in range(0, len(h), w)))
        else:
            parts.append(''.join(cmap.get(ch, chr(ch)) for ch in unesc(p[1])))
    return ''.join(parts)

out = []
for _, cnum, rmap in pages:
    items = []; cmap, nb = {}, 1; TL = 0.0
    a = d = 1.0; b = c = e = f = 0.0
    for t in TOK.finditer(stream_of(cnum)):
        g = t.group(0)
        if t.group(1):
            cmap, nb = rmap.get(t.group(1).decode(), ({}, 1))
        elif t.group(4):
            tx, ty = float(t.group(2)), float(t.group(3))
            if t.group(4) == b'TD': TL = -ty
            e, f = tx*a + ty*c + e, tx*b + ty*d + f
        elif t.group(5) is not None:
            a, b, c, d, e, f = [float(t.group(i)) for i in range(5, 11)]
        elif t.group(11):
            TL = float(t.group(11))
        elif g == b'T*':
            e, f = (-TL)*c + e, (-TL)*d + f
        elif g == b'BT':
            a = d = 1.0; b = c = e = f = 0.0
        else:
            s = show(t.group(12) if t.group(12) is not None else t.group(13), cmap, nb)
            if s: items.append((e, f, s))
    if not items: continue
    band = PW / NCOL
    for ci in range(NCOL):
        col = sorted((i for i in items if ci*band <= i[0] < (ci+1)*band),
                     key=lambda i: (-round(i[1]/3), i[0]))
        line, last = [], None
        for _, yy, s in col:
            if last is not None and abs(yy - last) > 2.5:
                out.append(''.join(line)); line = []
            line.append(s); last = yy
        if line: out.append(''.join(line))
    out.append('')
print('\n'.join(out))
