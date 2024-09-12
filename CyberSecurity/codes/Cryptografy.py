from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

#Generate key and vector to init (IV)
key = os.urandom(32) #generate a key of 256 bits
iv = os.urandom(16) #genarete a IV of 128 bits

#Data to be cryptografied
data = b"Confidencial Data"

#Cryptography

cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
cryptografied_data = encryptor.update(data) + encryptor.finalize()

print(f"Cryptografied Data: {cryptografied_data}")

#Decryptation
decryptor = cipher.decryptor()
original_data = decryptor.update(cryptografied_data) + decryptor.finalize()

print(f"Original Data: {original_data}")


