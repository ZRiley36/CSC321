from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto.Hash import SHA256
from Crypto.Util import Padding

class DHUser:
    def __init__(self, q, alpha, iv):
        self.secret_key = None
        self.iv = iv
        self.q = q
        self.alpha = alpha
        self.private_key = random.randint(0, q)
        self.public_key = pow(alpha, self.private_key, q)

    def compute_secret_key(self, other_public_key):
        self.secret_key = SHA256.new(
            pow(other_public_key, self.private_key, self.q).to_bytes(length=16)
        ).hexdigest()[0:16]

    def encrypt_message(self, message):
        cbc = AES.new(bytes(self.secret_key, "utf-8"), AES.MODE_CBC, iv=self.iv)
        padded = Padding.pad(bytes(message, "utf-8"), 16)
        return cbc.encrypt(padded)

    def decrypt_message(self, cypher_text):
        cbc = AES.new(bytes(self.secret_key, "utf-8"), AES.MODE_CBC, iv=self.iv)
        return Padding.unpad(cbc.decrypt(cypher_text), 16)
