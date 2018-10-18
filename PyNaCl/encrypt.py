import nacl.secret
import nacl.utils

# This must be kept secret, this is the combination to your safe
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# This is your safe, you can use it to encrypt or decrypt messages
box = nacl.secret.SecretBox(key)

try:
    textToEncrypt = input('Enter text to be encrypted: ').encode()
except ValueError:
    print('Invalid input.')

print('Message: ', textToEncrypt)
# Encrypt our message, it will be exactly 40 bytes longer than the
#   original message as it stores authentication information and the
#   nonce alongside it.
nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
encrypted = box.encrypt(textToEncrypt)

print('Encrypted message: ', encrypted)

decrypted = box.decrypt(encrypted)
print('Decrypted message: ', decrypted)
