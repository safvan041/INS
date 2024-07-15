import numpy as np

# Function to find the multiplicative inverse in modulo 26
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to find the inverse of the key matrix in modulo 26
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = mod_inverse(det % modulus, modulus)  # Multiplicative inverse of the determinant
    
    if det_inv is None:
        raise ValueError("The key matrix is not invertible in modulo 26")
    
    # Matrix of cofactors, transposed (i.e., the adjugate matrix)
    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_inv

# Function to encrypt the plaintext using Hill cipher
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    n = key_matrix.shape[0]
    padding_length = (n - len(plaintext) % n) % n
    plaintext += 'X' * padding_length  # Padding with 'X' if necessary
    
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, n).T
    
    ciphertext_matrix = key_matrix @ plaintext_matrix % 26
    ciphertext_vector = ciphertext_matrix.T.flatten()
    
    ciphertext = ''.join(chr(int(num) + ord('A')) for num in ciphertext_vector)
    return ciphertext

# Function to decrypt the ciphertext using Hill cipher
def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    n = key_matrix.shape[0]
    
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, n).T
    
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)
    plaintext_matrix = key_matrix_inv @ ciphertext_matrix % 26
    plaintext_vector = plaintext_matrix.T.flatten()
    
    plaintext = ''.join(chr(int(num) + ord('A')) for num in plaintext_vector)
    return plaintext

# Main function to demonstrate Hill cipher encryption and decryption
def main():
    key_matrix = np.array([[9, 4], [5, 7]])
    plaintext = "ATTACK AT ONCE"
    
    print("Key Matrix:")
    print(key_matrix)
    
    encrypted = hill_encrypt(plaintext, key_matrix)
    print("\nEncrypted Text:", encrypted)
    
    decrypted = hill_decrypt(encrypted, key_matrix)
    print("\nDecrypted Text:", decrypted)

if __name__ == "__main__":
    main()
