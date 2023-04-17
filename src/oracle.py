from Crypto import Random
from Crypto.Cipher import AES
import cbc
import sys

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
    return cbc.encrypt(filename, key, iv) 
# padding happens in cbc encrypt
# need to refactor csc encrypt so it can return the cipher text
# still havent flipped bits of cipher text to include substring ";admin=true;"
    
    
    
def verify(key, iv, ciphertext):
    substring = ";admin=true;"
    cipher = AES.new(key, AES.MODE_EBC, iv)
    plaintext  = cipher.decrypt(ciphertext)
    if substring in plaintext:
        return cipher.verify()
    return False
   

def main():
    key = Random.get_random_bytes(16)
    iv = Random.get_random_bytes(16)
    usrdata  = input('submit your message: ')
    submit(key, iv, usrdata)


if __name__ == "__main__":
    main()
