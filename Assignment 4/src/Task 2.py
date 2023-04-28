import bcrypt
import time
from nltk.corpus import words


def main():
    sorted_words = sorted(words.words(), key=lambda s: len(s))
    f = open('./passwords.txt', 'r')
    lines = f.readlines()
    for line in lines:
        split = line.split(':')
        crack_password(
            user=split[0],
            data=split[1],
            sorted_words=sorted_words
        )


def crack_password(user, data, sorted_words):
    split_data = data.split("$")
    print("name: ", user)
    print("algorithm: ", split_data[1])
    print("workfactor: ", split_data[2])
    print("salt: ", split_data[3][:22])
    print("hash: ", split_data[3][22:])
    start = time.time()

    for word in sorted_words:
        if 6 <= len(word) <= 10:
            result = bcrypt.hashpw(bytes(word, "utf-8"), bytes(data[:29], "utf-8"))
            if str(result) == data:
                end = time.time()
                print("Password found: ", word)
                print("Total time: ", (end-start) / 60.0, " minutes")

if __name__ == "__main__":
    main()
