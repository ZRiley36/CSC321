from Crypto.Util import number


def calc_d(totient, e):
    test = totient + 1
    while test % e != 0:
        test += totient
    return test // e


def RSA():
    e = 65537
    # Variable length primes
    num_length = 2048
    p = number.getPrime(num_length)
    q = number.getPrime(num_length)
    n = p * q
    o = (p - 1) * (q - 1)
    d = calc_d(o, e)
    PU = (e, n)
    PR = (d, n)
    # encrypt
    plain_text_input = "hello world"
    print("Plain text message: ", plain_text_input)
    int_message = int.from_bytes(plain_text_input.encode(), byteorder='little')
    print("Message as integer: ", int_message)

    cipher_text = pow(int_message, e, n)
    print("encrypted message: ", cipher_text)

    decrypted_text = pow(cipher_text, d, n)
    print("decrypted message as integer: ", decrypted_text)
    original_message = decrypted_text.to_bytes(byteorder='little', length=len(plain_text_input)).decode()
    print("Back to plain text: ", original_message)


if __name__ == "__main__":
    RSA()
