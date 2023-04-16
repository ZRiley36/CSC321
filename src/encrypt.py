from Crypto import Random
from src import ecb, cbc
import sys

def main():
    # Expects [mode] [file]
    # mode is either ecb (-e) or cbc (-c)
    if len(sys.argv) != 3:
        print("Usage: encrypt [mode] [file]")
    mode = sys.argv[1]
    filename = sys.argv[2]
    key = Random.get_random_bytes(16)
    if mode == "-e":
        ecb.encrypt(filename, key)
        print("Key = ", key)
    elif mode == "-c":
        iv = Random.get_random_bytes(16)
        cbc.encrypt(filename, key, iv)


if __name__ == "__main__":
    main()
