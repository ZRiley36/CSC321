from Crypto import Random
from src import ecb, cbc
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: encrypt [file]")
    filename = sys.argv[1]
    key = Random.get_random_bytes(16)
    ecb.encrypt(filename, key)
    iv = Random.get_random_bytes(16)
    cbc.encrypt(filename, key, iv)
    print("Key = ", key)


if __name__ == "__main__":
    main()
