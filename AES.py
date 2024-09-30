from Crypto.Cipher import AES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
from Crypto.Random import get_random_bytes # type: ignore

def aes_encrypt(plain_text, key):
    # Ensure the key size is either 16, 24, or 32 bytes for AES
    key = key.ljust(32)[:32]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    return cipher.iv, cipher_text

def aes_decrypt(cipher_text, key, iv):
    key = key.ljust(32)[:32]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plain_text.decode('utf-8')

def main():
    plain_text = "Hello, folks!"
    key = "newkey"

    print("Original Text:", plain_text)
    print("Key:", key)

    # Encrypt
    iv, cipher_text = aes_encrypt(plain_text, key)
    print("IV:", iv.hex())
    print("Cipher Text:", cipher_text.hex())

    # Decrypt
    decrypted_text = aes_decrypt(cipher_text, key, iv)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
