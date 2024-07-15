def create_matrix(text, key_length):
    matrix = []
    for i in range(0, len(text), key_length):
        row = list(text[i:i + key_length])
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def columnar_transposition_encrypt(plaintext, key):
    key_length = len(key)
    plaintext = plaintext.replace(" ", "").upper()
    padding_length = (key_length - len(plaintext) % key_length) % key_length
    plaintext += 'X' * padding_length
    
    matrix = create_matrix(plaintext, key_length)
    transposed_matrix = transpose_matrix(matrix)
    
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''
    for index in key_indices:
        column = transposed_matrix[index]
        ciphertext += ''.join(column)
    
    return ciphertext

def columnar_transposition_decrypt(ciphertext, key):
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    matrix = create_matrix(ciphertext, num_rows)
    transposed_matrix = transpose_matrix(matrix)
    
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    decrypted_matrix = [[] for _ in range(num_rows)]
    
    for i, index in enumerate(key_indices):
        for j in range(num_rows):
            decrypted_matrix[j].append(transposed_matrix[i][j])
    
    plaintext = ''.join([''.join(row) for row in decrypted_matrix])
    return plaintext.rstrip('X')

def main():
    key = "4312567"
    plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    
    print("Key:", key)
    print("Plaintext:", plaintext)
    
    encrypted = columnar_transposition_encrypt(plaintext, key)
    print("\nEncrypted Text:", encrypted)
    
    decrypted = columnar_transposition_decrypt(encrypted, key)
    print("\nDecrypted Text:", decrypted)

if __name__ == "__main__":
    main()
