en_alphabet = "abcdefghijklmnopqrstuvwxyz"

#
# This function returns true if and only if the character c is an
# alphabetic character in the English alphabet
#
def is_alphabetic_char(c):
    return (c.lower() in en_alphabet)
#
# This function converts a single character into its numeric value
#
def char_to_num(c):
    return en_alphabet.index(c.lower())
#
# This function returns the character corresponding to x mod 26
# in the English alphabet
#
def num_to_char(x):
    return en_alphabet[x % 26]

def CaesarEncrypt(k, plaintext):
    ciphertext = ""
    for c in plaintext:
	    if is_alphabetic_char(c):
	        number = char_to_num(c)+k
	        ciphertext += num_to_char(number)
 
    return ciphertext


def CaesarDecrypt(k, ciphertext):
    plaintext = ""
    for c in ciphertext:
        number = char_to_num(c)
        plaintext += num_to_char(number-k)

    return plaintext

key = 3
encrypted = CaesarEncrypt(key, "meet me after the toga party")
print('Encrypted: ', encrypted)

decrypted = CaesarDecrypt(key, encrypted)
print('Decrypted: ', decrypted)















