from Crypto import Random
from Crypto.Cipher import AES
from typing import ByteString
import cbc
import sys

BMP_HEADER_LENGTH = 54
# 128 bit/16 bytes
BLOCK_SIZE = 16


def byteflip(ciphertext):
    ciphertext[2] = chr(ord(ciphertext[2]) ^ ord('%=3b') ^ ord ('='))
    return ciphertext

def encrypt(
        filename: str,
        key: ByteString,
        iv: ByteString
):
    f = open(filename, mode="rb")
    cipher = AES.new(key, AES.MODE_ECB)
    next_block = f.read(BLOCK_SIZE)
    result_block = bytes(list(iv))
    result = bytes()
    while next_block:
        if len(next_block) != BLOCK_SIZE:
            # padding
            n = BLOCK_SIZE - len(next_block)
            for i in range(n):
                next_block += bytes([n])

        result_block = cipher.encrypt(cbc.bxor(next_block, result_block))
        result += result_block
        next_block = f.read(BLOCK_SIZE)
    f.close()
    return result


def urlEncode(data):
    data = data.replace(';', '%3b')
    data = data.replace('=', '%3d')
    return data
            
        
def submit(key, iv, data):
    filename = "oraclestr.txt"
    prepend = "userid-456;userdata="
    appendstr = ";session-id-31337"
    data = urlEncode(data)
    concatstr = prepend+data+appendstr
    byteflip(concatstr)
    f = open(filename, 'w')
    f.write(concatstr)
    f.close()
    return encrypt(filename, key, iv) 
# padding happens in cbc encrypt
# need to refactor cbc encrypt so it can return the cipher text
# still havent flipped bits of cipher text to verify substring ";admin=true;"
    
def verify(key, iv, ciphertext):
    substring = ";admin=true;"
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext  = cipher.decrypt(ciphertext).decode("UTF-8")
    print(plaintext)
    if substring in str(plaintext):
        return True
    return False
   

def main():
    key = Random.get_random_bytes(16)
    iv = Random.get_random_bytes(16)
    usrdata  = input('submit your message: ')
    ciphertext = submit(key, iv, usrdata)
    print(verify(key, iv, ciphertext))


if __name__ == "__main__":
    main()
