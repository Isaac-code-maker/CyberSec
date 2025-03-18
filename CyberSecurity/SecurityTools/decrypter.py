import os
import pyaes

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#chave de descriptografia

key = b'1234567890123456'

aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)


#remover o arquivo criptografado

os.remove(file_name)

#criar um novo arquivo com os dados descriptografados

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()
                