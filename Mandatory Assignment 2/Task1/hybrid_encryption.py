import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, SealedBox

# Generate Bob's private key, as we've done in the Box example
skbob = PrivateKey.generate()
pkbob = skbob.public_key

# Alice wishes to send a encrypted message to Bob,
# but prefers the message to be untraceable
sealed_box = SealedBox(pkbob)

# This is the key to be shared by both parties(encrypted with the other's public key)
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Encrypt the message, it will carry the ephemeral key public part
# to let Bob decrypt it
encryptedKey = sealed_box.encrypt(key)

print("Common key: ", key, "\n")
print('Alice sends:', encryptedKey, "\n")

# Bob decrypts key
unseal_box = SealedBox(skbob)
decryptedKey = unseal_box.decrypt(encryptedKey)

print('Bob receives:', encryptedKey, "\n")
print('Bob decrypts:', decryptedKey, "\n")

# Let the messaging begin!
box = nacl.secret.SecretBox(decryptedKey)

message = b"Received our new key. The president will be exiting through the lower levels."

encryptedM = box.encrypt(message)

print('Original Message: ', message, '\n')
print('Bob sends: ', encryptedM, '\n')

# Alice decrypts
decryptedM = box.decrypt(encryptedM)

print('Alice receives:', encryptedM, "\n")
print('Alice decrypts:', decryptedM, "\n")

# Questions 
# Q1: Could we have done it the other way around, first using symmetric
# encryption and then switching to asymmetric encryption? Explain your
# answer.
# A1: It could have been done but sending encrypted messages would be a lot slower with the asymmetric encryption.
# Encrypting the secret and public keys wouldn't make sense because the public keys are already shared or known 
# and the secret keys wouldn't need to be shared.

# Q2: What do you think of the security of the system? Do you think there’s
# any possible attack? If so, describe it and explain how we could prevent it.
# A2: We think the system is very secure as we are using asymmetric encryption to share the key needed to decrypt 
# the message but if we use a nonce which is too short or repeats it's digits it would be easier to crack and also
# if we use too short public or secret keys it is also a security hazard as the encryption would be cracked way easier