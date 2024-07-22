import os

def generate_key(length):
    """Generate a key of specified length with truly random bytes."""
    return os.urandom(length)

def otp_encrypt(plaintext, key):
    """Encrypt the plaintext using the one-time pad key."""
    plaintext_bytes = plaintext.encode('utf-8')
    ciphertext_bytes = bytes([pt ^ k for pt, k in zip(plaintext_bytes, key)])
    return ciphertext_bytes

def otp_decrypt(ciphertext, key):
    """Decrypt the ciphertext using the one-time pad key."""
    plaintext_bytes = bytes([ct ^ k for ct, k in zip(ciphertext, key)])
    return plaintext_bytes.decode('utf-8')

def main():
    plaintext = "attack at once"
    print("Plaintext:", plaintext)

    # Generate a key that is the same length as the plaintext
    key = generate_key(len(plaintext))
    print("Key:", key.hex())

    # Encrypt the plaintext
    ciphertext = otp_encrypt(plaintext, key)
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt the ciphertext
    decrypted_text = otp_decrypt(ciphertext, key)

if __name__ == "__main__":
    main()
