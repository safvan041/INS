def encrypt(msg,key):
	result = ""

	for i in range(len(msg)):
		char = msg[i]

		if (char.isupper()):
			result += chr((ord(char) + key-65) % 26 + 65)

		else:
			result += chr((ord(char) + key - 97) % 26 + 97)
	return result

msg = "ATTACKATONCE"
key = 4
print ("Text : " + msg)
print ("Shift : " + str(key))
print ("Cipher: " + encrypt(msg,key))
print ("decrypted_msg: " + msg)
