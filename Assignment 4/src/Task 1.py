from Crypto import Random
from Crypto.Hash import SHA256
from bitstring import BitArray
import random
import string

def hash_message_size(m, k):
    m = bytes(m, 'utf-8')
    return(SHA256.new(m).digest()[:k:])
    
def hamming_dist_one(a):
    b = a[::1]
    b[-1] = chr(ord(a[-1]) + 1)
    a = ''.join(a)
    b = ''.join(b)
    print(f"b: {b} a: {a}")
    print(hash_message_size(a, 2))
    print(hash_message_size(b, 2))

def find_collision(a):
    digest_size = 1
    while True: 
        b = ''.join(random.choices(string.ascii_lowercase, k=5))
        if (hash_message_size(a, digest_size) == hash_message_size(b, digest_size)):
            print(hash_message_size(a, digest_size), a, hash_message_size(b, digest_size), b)
            return None
        

def main():
    a = list("hello")
    hamming_dist_one(a)
    find_collision("potato")


if __name__ == "__main__":
    main()