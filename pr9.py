from Crypto.Util import number
from Crypto.Random import get_random_bytes

def generate_keypair(bits=1024):
    p = number.getPrime(bits // 2)
    q = number.getPrime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = number.inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_int = int.from_bytes(plaintext_bytes, byteorder='big')
    cipher_int = pow(plaintext_int, e, n)
    return cipher_int

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big')
    return plaintext_bytes.decode('utf-8')

def main():
    message = "Hello, folks!"
    print("Original Message:", message)
    
    # Generate RSA key pair
    public_key, private_key = generate_keypair()
    
    # Encrypt the message
    cipher_text = encrypt(public_key, message)
    print("Cipher Text:", cipher_text)
    
    # Decrypt the message
    decrypted_message = decrypt(private_key, cipher_text)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
