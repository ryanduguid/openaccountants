"""Known-answer tests for scripts/pdf_aes.py.

The module's docstring quoted the FIPS-197 vectors it was checked against;
nothing ran them. These are those vectors (Appendix C.1, C.2 and C.3), the
NIST SP 800-38A CBC vectors (F.2.1 and F.2.2), and the module's own
whole-block contract.
"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

SPEC = importlib.util.spec_from_file_location("pdf_aes", SCRIPTS / "pdf_aes.py")
assert SPEC is not None and SPEC.loader is not None
pdf_aes = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pdf_aes)

PLAINTEXT = bytes.fromhex("00112233445566778899aabbccddeeff")
#: FIPS-197 Appendix C: key length -> (key, expected ciphertext of PLAINTEXT).
FIPS_197 = {
    128: (bytes(range(16)), "69c4e0d86a7b0430d8cdb78070b4c55a"),
    192: (bytes(range(24)), "dda97ca4864cdfe06eaf70a0ec0d7191"),
    256: (bytes(range(32)), "8ea2b7ca516745bfeafc49904b496089"),
}
#: NIST SP 800-38A F.2.1 / F.2.2 (CBC-AES128): four blocks under one IV.
CBC_KEY = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
CBC_IV = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
CBC_PLAIN = bytes.fromhex(
    "6bc1bee22e409f96e93d7e117393172a"
    "ae2d8a571e03ac9c9eb76fac45af8e51"
    "30c81c46a35ce411e5fbc1191a0a52ef"
    "f69f2445df4f9b17ad2b417be66c3710"
)
CBC_CIPHER = bytes.fromhex(
    "7649abac8119b246cee98e9b12e9197d"
    "5086cb9b507219ee95db113a917678b2"
    "73bed6b8e3c1743b7116e69e22229516"
    "3ff1caa1681fac09120eca307586e1a7"
)


class BlockCipherTests(unittest.TestCase):
    def test_fips_197_known_answers(self) -> None:
        for bits, (key, expected) in FIPS_197.items():
            with self.subTest(bits=bits):
                w, nr = pdf_aes._expand(key)
                self.assertEqual(nr, {128: 10, 192: 12, 256: 14}[bits])
                cipher = pdf_aes._encrypt_block(PLAINTEXT, w, nr)
                self.assertEqual(cipher.hex(), expected)
                self.assertEqual(pdf_aes._decrypt_block(cipher, w, nr), PLAINTEXT)


class CbcTests(unittest.TestCase):
    def test_sp800_38a_cbc_vectors(self) -> None:
        self.assertEqual(pdf_aes.cbc_encrypt(CBC_KEY, CBC_IV, CBC_PLAIN), CBC_CIPHER)
        self.assertEqual(pdf_aes.cbc_decrypt(CBC_KEY, CBC_IV, CBC_CIPHER), CBC_PLAIN)

    def test_round_trip_with_every_key_length(self) -> None:
        data = bytes(range(256))[:64]
        for bits, (key, _) in FIPS_197.items():
            with self.subTest(bits=bits):
                cipher = pdf_aes.cbc_encrypt(key, CBC_IV, data)
                self.assertEqual(len(cipher), len(data))
                self.assertNotEqual(cipher, data)
                self.assertEqual(pdf_aes.cbc_decrypt(key, CBC_IV, cipher), data)

    def test_only_whole_blocks_are_processed(self) -> None:
        """PDF streams are padded to the block size; a trailing partial block is
        neither encrypted nor invented."""
        self.assertEqual(pdf_aes.cbc_encrypt(CBC_KEY, CBC_IV, b""), b"")
        self.assertEqual(pdf_aes.cbc_encrypt(CBC_KEY, CBC_IV, CBC_PLAIN[:16] + b"tail"), CBC_CIPHER[:16])
        self.assertEqual(pdf_aes.cbc_decrypt(CBC_KEY, CBC_IV, CBC_CIPHER[:16] + b"tail"), CBC_PLAIN[:16])

    def test_chaining_depends_on_the_iv(self) -> None:
        other_iv = bytes(16)
        self.assertNotEqual(pdf_aes.cbc_encrypt(CBC_KEY, other_iv, CBC_PLAIN), CBC_CIPHER)
        self.assertNotEqual(pdf_aes.cbc_decrypt(CBC_KEY, other_iv, CBC_CIPHER)[:16], CBC_PLAIN[:16])


if __name__ == "__main__":
    unittest.main()
