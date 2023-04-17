from Crypto import Random
from Crypto.Cipher import AES
from typing import ByteString
import cbc
import sys

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
    next_block = f.read(BLOCK_SIZE)
    result_block = bytes(list(iv))
    result
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
    data = data.replace(';', '%3B')
    data = data.replace('=', '%3D')
    return data
            
        
def submit(key, iv, data):
    filename = "oraclestr.txt"
    prepend = "userid-456;userdata="
    appendstr = ";session-id-31337"
    data = urlEncode(data)
    concatstr = prepend+data+appendstr
    f = open(filename, 'w')
    f.write(concatstr)
    f.close()
    return encrypt(filename, key, iv) 
# padding happens in cbc encrypt
# need to refactor csc encrypt so it can return the cipher text
# still havent flipped bits of cipher text to include substring ";admin=true;"
    
def verify(key, iv, ciphertext):
    substring = ";admin=true;"
    cipher = AES.new(key, AES.MODE_EAX, iv)
    plaintext  = cipher.decrypt(ciphertext.c_str())
    if substring in plaintext:
        return cipher.verify()
    return False
   

def main():
    key = Random.get_random_bytes(16)
    iv = Random.get_random_bytes(16)
    usrdata  = input('submit your message: ')
    ciphertext = submit(key, iv, usrdata)
    verify(key, iv, ciphertext)


if __name__ == "__main__":
    main()
