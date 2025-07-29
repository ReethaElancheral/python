# passwordmanager/security.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
import random
import string

class AESCipher:
    def __init__(self, key):
        if not isinstance(key, bytes) or len(key) not in (16, 24, 32):
            raise ValueError("Encryption key must be bytes of length 16, 24, or 32.")
        self.key = key
        self.backend = default_backend()

    def encrypt(self, plaintext):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ct = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return base64.b64encode(iv + ct).decode()

    def decrypt(self, ciphertext):
        raw = base64.b64decode(ciphertext)
        iv = raw[:16]
        ct = raw[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        pt = decryptor.update(ct) + decryptor.finalize()
        return pt.decode()

def generate_strong_password(length=16):
    if length < 8:
        length = 8
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
