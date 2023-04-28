import threading
import bcrypt
import time
from nltk.corpus import words

global found


def main():
    sorted_words = sorted(words.words(), key=lambda s: len(s))
    f = open('./passwords.txt', 'r')
    lines = f.readlines()
    start = time.time()
    for line in lines:
        split = line.split(':')
        crack_password(
            user=split[0],
            data=split[1],
            sorted_words=sorted_words
        )
    end = time.time()
    print("Total time:", (end - start) / 60.0, "minutes")


def crack_password(user, data, sorted_words):
    global found
    found = False
    if data.endswith("\n"):
        data = data.removesuffix("\n")
    print("Name: ", user)
    start = time.time()
    for word in sorted_words:
        if found:
            break
        if 6 <= len(word) <= 10:
            thread = threading.Thread(target=thread_fun, args=(word, data, start))
            thread.start()
        if len(word) > 10:
            break


# 2:35

def thread_fun(word, data, start):
    global found
    result = bcrypt.hashpw(bytes(word, "utf-8"), bytes(data[:29], "utf-8"))
    if result == bytes(data, "utf-8"):
        end = time.time()
        print("Password:", word)
        print("Total time:", (end - start) / 60.0, "minutes\n")
        found = True


if __name__ == "__main__":
    main()
