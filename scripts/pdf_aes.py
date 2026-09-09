"""Minimal pure-Python AES-CBC (128/192/256). No dependencies.

Used by `read-tax-pdf.py` to open AES-encrypted tax-authority PDFs with an
empty user password. It exists because this environment's `cryptography` and
`pypdf` both fail on a broken `_cffi_backend`, and several state revenue
departments ship their forms encrypted.

Verified against the FIPS-197 known-answer vectors for AES-128 and AES-256:

    key 000102...0f, plaintext 00112233445566778899aabbccddeeff
      -> 69c4e0d86a7b0430d8cdb78070b4c55a   (AES-128)
    key 000102...1f, same plaintext
      -> 8ea2b7ca516745bfeafc49904b496089   (AES-256)

Correctness only; it makes no attempt at constant-time execution and must not
be used for anything security-sensitive.
"""
_SBOX = []
_INV = []
def _init():
    p = q = 1
    sbox = [0] * 256
    while True:
        p = p ^ ((p << 1) & 0xFF) ^ (0x1B if p & 0x80 else 0)
        q ^= q << 1; q ^= q << 2; q ^= q << 4; q &= 0xFF
        if q & 0x80: q ^= 0x09
        x = q ^ ((q << 1) | (q >> 7)) ^ ((q << 2) | (q >> 6)) ^ ((q << 3) | (q >> 5)) ^ ((q << 4) | (q >> 4))
        sbox[p] = (x ^ 0x63) & 0xFF
        if p == 1: break
    sbox[0] = 0x63
    _SBOX.extend(sbox)
    inv = [0] * 256
    for i, v in enumerate(sbox): inv[v] = i
    _INV.extend(inv)
_init()

def _xt(a):
    a <<= 1
    return (a ^ 0x1B) & 0xFF if a & 0x100 else a

def _mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a = _xt(a); b >>= 1
    return r

_RCON = [0x01]
for _ in range(13): _RCON.append(_xt(_RCON[-1]))

def _expand(key):
    nk = len(key) // 4
    nr = nk + 6
    w = [list(key[4 * i:4 * i + 4]) for i in range(nk)]
    for i in range(nk, 4 * (nr + 1)):
        t = list(w[i - 1])
        if i % nk == 0:
            t = t[1:] + t[:1]
            t = [_SBOX[b] for b in t]
            t[0] ^= _RCON[i // nk - 1]
        elif nk > 6 and i % nk == 4:
            t = [_SBOX[b] for b in t]
        w.append([w[i - nk][j] ^ t[j] for j in range(4)])
    return w, nr

def _addrk(st, w, r):
    for c in range(4):
        for j in range(4):
            st[c][j] ^= w[r * 4 + c][j]

def _encrypt_block(blk, w, nr):
    st = [list(blk[4 * c:4 * c + 4]) for c in range(4)]
    _addrk(st, w, 0)
    for rnd in range(1, nr + 1):
        for c in range(4):
            for j in range(4): st[c][j] = _SBOX[st[c][j]]
        st = [[st[c][r] for c in range(4)] for r in range(4)]          # rows
        for r in range(1, 4): st[r] = st[r][r:] + st[r][:r]            # shift
        st = [[st[r][c] for r in range(4)] for c in range(4)]          # cols
        if rnd != nr:
            for c in range(4):
                a = st[c]
                st[c] = [_mul(a[0],2)^_mul(a[1],3)^a[2]^a[3],
                         a[0]^_mul(a[1],2)^_mul(a[2],3)^a[3],
                         a[0]^a[1]^_mul(a[2],2)^_mul(a[3],3),
                         _mul(a[0],3)^a[1]^a[2]^_mul(a[3],2)]
        _addrk(st, w, rnd)
    return bytes(b for c in st for b in c)

def _decrypt_block(blk, w, nr):
    st = [list(blk[4 * c:4 * c + 4]) for c in range(4)]
    _addrk(st, w, nr)
    for rnd in range(nr - 1, -1, -1):
        st = [[st[c][r] for c in range(4)] for r in range(4)]
        for r in range(1, 4): st[r] = st[r][-r:] + st[r][:-r]
        st = [[st[r][c] for r in range(4)] for c in range(4)]
        for c in range(4):
            for j in range(4): st[c][j] = _INV[st[c][j]]
        _addrk(st, w, rnd)
        if rnd != 0:
            for c in range(4):
                a = st[c]
                st[c] = [_mul(a[0],14)^_mul(a[1],11)^_mul(a[2],13)^_mul(a[3],9),
                         _mul(a[0],9)^_mul(a[1],14)^_mul(a[2],11)^_mul(a[3],13),
                         _mul(a[0],13)^_mul(a[1],9)^_mul(a[2],14)^_mul(a[3],11),
                         _mul(a[0],11)^_mul(a[1],13)^_mul(a[2],9)^_mul(a[3],14)]
    return bytes(b for c in st for b in c)

def cbc_encrypt(key, iv, data):
    w, nr = _expand(key); out = bytearray(); prev = iv
    for i in range(0, len(data) - len(data) % 16, 16):
        blk = bytes(x ^ y for x, y in zip(data[i:i+16], prev))
        prev = _encrypt_block(blk, w, nr); out += prev
    return bytes(out)

def cbc_decrypt(key, iv, data):
    w, nr = _expand(key); out = bytearray(); prev = iv
    for i in range(0, len(data) - len(data) % 16, 16):
        c = data[i:i+16]
        out += bytes(x ^ y for x, y in zip(_decrypt_block(c, w, nr), prev)); prev = c
    return bytes(out)
