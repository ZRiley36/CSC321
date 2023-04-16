from typing import ByteString
from Crypto.Cipher import AES

BMP_HEADER_LENGTH = 54
# 128 bit/16 bytes
BLOCK_SIZE = 16


def encrypt(
        filename: str,
        key: ByteString
):
    f = open(filename, mode="rb")
    header = f.read(BMP_HEADER_LENGTH)
    cipher = AES.new(key, AES.MODE_ECB)

    result = open("ecb_result.bmp", "wb")
    result.write(header)

    next_block = f.read(BLOCK_SIZE)
    while next_block:
        if len(next_block) != BLOCK_SIZE:
            # padding
            n = BLOCK_SIZE - len(next_block)
            for i in range(n):
                next_block += bytes([n])

        result.write(cipher.encrypt(next_block))
        next_block = f.read(BLOCK_SIZE)

    f.close()
    result.close()
