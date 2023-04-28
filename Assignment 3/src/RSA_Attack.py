from Crypto.Util import number, Padding
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Random import random


def calc_d(totient, e):
    test = totient + 1
    while test % e != 0:
        test += totient
    return test // e


def RSA():
    # Alice generates n and e
    e = 65537
    num_length = 2048
    p = number.getPrime(num_length)
    q = number.getPrime(num_length)
    n = p * q
    o = (p - 1) * (q - 1)
    d = calc_d(o, e)
    iv = Random.get_random_bytes(16)

    # Alice gives out n and e to Bob, who chooses a secret key and encrypts it using RSA
    secret_key_from_bob = random.randint(0, n)
    encrypted_secret_key_from_bob = pow(secret_key_from_bob, e, n)

    # Mallory then intercepts the encrypted key from bob
    # In order to then access Alice's message later, Mallory edits the encrypted key
    encrypted_secret_key_from_bob = 0

    # Alice then decrypts the key using RSA
    decrypted_secret_key = pow(encrypted_secret_key_from_bob, d, n)
    hashed_secret_key = SHA256.new(decrypted_secret_key.to_bytes(length=num_length, byteorder="big")).hexdigest()[0:16]
    message_to_bob = "Hi Bob!"
    alice_cbc = AES.new(bytes(hashed_secret_key, "utf-8"), AES.MODE_CBC, iv=iv)
    padded = Padding.pad(bytes(message_to_bob, "utf-8"), 16)
    encrypted_message_to_bob = alice_cbc.encrypt(padded)

    # Because mallory edited the encrypted_secret_key_from_bob, she knows that the decrypted version is just equal to 0
    # With this she can decrypt the message
    mallory_cbc = AES.new(
        bytes(SHA256.new(int(0).to_bytes(length=num_length, byteorder="big")).hexdigest()[0:16], "utf-8"), AES.MODE_CBC,
        iv)
    decrypted_message = Padding.unpad(mallory_cbc.decrypt(encrypted_message_to_bob), 16).decode("utf-8")
    print("Mallory recieved: ", decrypted_message)


if __name__ == "__main__":
    RSA()
