import string

# Function to decrypt the Caesar cipher with a given key
def decrypt_caesar(ciphertext, key):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Frequency analysis attack
def frequency_analysis_attack(ciphertext):
    # English letter frequencies (approximate)
    english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    # Count the frequency of each letter in the ciphertext
    letter_counts = {char: 0 for char in string.ascii_uppercase}
    for char in ciphertext.upper():
        if char in letter_counts:
            letter_counts[char] += 1

    # Sort the letters by frequency
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)

    # Attempt to decrypt by matching the most frequent letter in ciphertext to 'E'
    potential_plaintexts = []
    for i in range(len(english_freq_order)):
        key = (ord(sorted_letters[i]) - ord('E')) % 26
        decrypted_text = decrypt_caesar(ciphertext, key)
        potential_plaintexts.append((key, decrypted_text))

    return potential_plaintexts

# Example ciphertext (encrypted with a shift of 3)
ciphertext = "DWWDFN DW RQFH"  # "HELLO WORLD"

# Perform the frequency analysis attack
potential_plaintexts = frequency_analysis_attack(ciphertext)

# Print the potential plaintexts and their corresponding keys
print("Potential decryptions:")
for key, plaintext in potential_plaintexts:
    print(f"Key: {key}, Plaintext: {plaintext}")
