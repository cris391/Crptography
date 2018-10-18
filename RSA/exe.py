import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

def encrypt(string):
    a = string
    new_string = ''
    for x in a:
        new_string = new_string+str(ord(x))+' '
    return new_string
encryptedA = int(encrypt('A'));

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('encryptedA', 32)
#message to encrypt is in the above line 'encrypt this message'

print('encrypted message:', encrypted) #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted'), decrypted

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()





    
# def unencrypt(string):
#     a = string
#     new_string = ''
#     b = a.split()
#     for x in b:
#         new_string = new_string+chr(int(x))
#     return new_string