from Crypto import Random
from Crypto.Hash import SHA256

from dh_user import DHUser

BIG_Q = \
    "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C6" \
    "9A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C0" \
    "13ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD70" \
    "98488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0" \
    "A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708" \
    "DF1FB2BC2E4A4371"

BIG_ALPHA = \
    "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507F" \
    "D6406CFF14266D31266FEA1E5C41564B777E690F5504F213" \
    "160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1" \
    "909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A" \
    "D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24" \
    "855E6EEB22B3B2E5"


def mitm_dh():
    iv = Random.get_random_bytes(16)
    alice = DHUser(q=int(BIG_Q, 16), alpha=int(BIG_Q, 16), iv=iv)
    mallory = DHUser(q=alice.q, alpha=alice.alpha, iv=iv)
    bob = DHUser(q=mallory.q, alpha=mallory.alpha, iv=iv)

    alice.compute_secret_key(mallory.public_key)
    bob.compute_secret_key(mallory.public_key)

    print("Bob's: ", bob.secret_key)
    print("Alice's: ", alice.secret_key)

    # In the special case where mallory has tampered with alpha to set it to Q, then
    # mallory can know the secret key is always 0 (before sha256)
    mallory_special_secret_key = SHA256.new(int(0).to_bytes(length=128, byteorder="big")).hexdigest()[0:16]
    print("Mallory knows the secret key is: ", mallory_special_secret_key)

    alice_cypher_text = alice.encrypt_message("Hi Bob!", alice.secret_key)
    alice_plain_text = mallory.decrypt_message(alice_cypher_text, mallory_special_secret_key)
    # alice_plain_text = alice_plain_text.decode('utf-8')
    alice_plain_text = str(alice_plain_text.decode('utf-8'))

    print("Mallory received: ", alice_plain_text)
    mallory_cipher_text = mallory.encrypt_message(alice_plain_text, mallory_special_secret_key)

    print("Bob received: ", bob.decrypt_message(mallory_cipher_text, bob.secret_key))

    bob_cipher_text = bob.encrypt_message("Hi Alice!", bob.secret_key)
    bob_plain_text = mallory.decrypt_message(bob_cipher_text, mallory_special_secret_key)

    bob_plain_text = str(bob_plain_text.decode('utf-8'))
    print("Mallory received: ", bob_plain_text)

    mallory_cipher_text = mallory.encrypt_message(bob_plain_text, mallory_special_secret_key)
    print("Alice received: ", alice.decrypt_message(mallory_cipher_text, alice.secret_key))


if __name__ == "__main__":
    mitm_dh()
