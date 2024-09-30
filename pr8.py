import random

def power_mod(base, exp, mod):
    """Modular exponentiation"""
    return pow(base, exp, mod)

def diffie_hellman():
    # Public parameters
    p = 23  # A small prime number
    g = 5   # A primitive root modulo p

    # Private keys
    a = random.randint(1, p-1)  # Private key for Party A
    b = random.randint(1, p-1)  # Private key for Party B

    # Public keys
    A = power_mod(g, a, p)  # Public key for Party A
    B = power_mod(g, b, p)  # Public key for Party B

    # Exchange public keys
    print("Party A's public key (A):", A)
    print("Party B's public key (B):", B)

    # Compute shared secret
    shared_secret_A = power_mod(B, a, p)  # Party A computes shared secret
    shared_secret_B = power_mod(A, b, p)  # Party B computes shared secret

    print("Shared secret computed by Party A:", shared_secret_A)
    print("Shared secret computed by Party B:", shared_secret_B)

    assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"

if __name__ == "__main__":
    diffie_hellman()
