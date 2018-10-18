from PIL import Image, ImageChops

plaintext = Image.open("./example/plaintext.jpeg", mode='r').convert("1") 
key = Image.open("./example/key.gif", mode='r').convert("1") 

encrypted = ImageChops.logical_xor(plaintext, key)

encrypted.save('encrypted.gif', 'GIF')

print(plaintext.format, plaintext.size, plaintext.mode)