from Crypto import Random

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


def simulate_dh():
    iv = Random.get_random_bytes(16)
    alice = DHUser(q=int(BIG_Q, 16), alpha=int(BIG_ALPHA, 16), iv=iv)
    bob = DHUser(q=int(BIG_Q, 16), alpha=int(BIG_ALPHA, 16), iv=iv)

    alice.compute_secret_key(bob.public_key)
    bob.compute_secret_key(alice.public_key)

    print("Bob's: ", bob.secret_key)
    print("Alice's: ", alice.secret_key)

    alice_cypher_text = alice.encrypt_message("Hi Bob!")
    print("Bob received: ", bob.decrypt_message(alice_cypher_text))

    bob_cypher_text = bob.encrypt_message("Hi Alice!")
    print("Alice received: ", alice.decrypt_message(bob_cypher_text))


if __name__ == "__main__":
    simulate_dh()
