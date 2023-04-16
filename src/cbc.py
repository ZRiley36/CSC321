from typing import ByteString
from Crypto.Cipher import AES

BMP_HEADER_LENGTH = 54
# 128 bit/16 bytes
BLOCK_SIZE = 16


def encrypt(
        filename: str,
        key: ByteString,
        iv: ByteString
):
    f = open(filename, mode="rb")
    header = f.read(BMP_HEADER_LENGTH)
    cipher = AES.new(key, AES.MODE_ECB)

    result = open("cbc_result.bmp", "wb")
    result.write(header)

    next_block = f.read(BLOCK_SIZE)
    result_block = bytes(list(iv))

    while next_block:
        if len(next_block) != BLOCK_SIZE:
            # padding
            n = BLOCK_SIZE - len(next_block)
            for i in range(n):
                next_block += bytes([n])

        result_block = cipher.encrypt(bxor(next_block, result_block))
        result.write(result_block)
        next_block = f.read(BLOCK_SIZE)

    f.close()
    result.close()


def bxor(b1, b2):  # use xor for bytes
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)
