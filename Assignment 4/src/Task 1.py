from Crypto import Random
from Crypto.Hash import SHA256
from bitstring import BitArray
import random
import string
import time


def hash_message_size(m, k):
    m = bytes(m, 'utf-8')
    return (BitArray(hex=SHA256.new(m).hexdigest())[:k:].bin)


def hamming_dist_one(a):
    b = a[::1]
    b[-1] = chr(ord(a[-1]) + 1)
    a = ''.join(a)
    b = ''.join(b)
    # print(f"b: {b} a: {a}")
    # print(hash_message_size(a, 256))
    # print(hash_message_size(b, 256))


def find_collision(a):
    digest_size = 32
    dict = {}
    count = 0
    start = time.time()
    while True:
        count += 1
        b = ''.join(random.choices(string.ascii_lowercase, k=5))
        h = hash_message_size(b, digest_size)
        if h in dict and dict[h] != b:
            end = time.time()
            print(
                f"found collision using {count} inputs in {end - start} seconds: {h} is the hash of {dict[h]} and {b}")
            return None
        dict[h] = b


def main():
    a = list("hamming distance of one")
    hamming_dist_one(a)
    find_collision("potato")


if __name__ == "__main__":
    main()
