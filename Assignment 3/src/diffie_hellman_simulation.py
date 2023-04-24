from Crypto import Random

from dh_user import DHUser


def simulate_dh():
    iv = Random.get_random_bytes(16)
    alice = DHUser(q=37, alpha=5, iv=iv)
    bob = DHUser(q=37, alpha=5, iv=iv)

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
