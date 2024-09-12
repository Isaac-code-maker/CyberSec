import string
import random

def gerarcifra():
    alfabeto = list(string.ascii_uppercase)
    alfabeto_cifrado = alfabeto[:]

    random.shuffle(alfabeto_cifrado)

    return dict(zip(alfabeto, alfabeto_cifrado))

def criptografia(texto, cifra):
    texto_cifrado = ""
    
    for char in texto.upper():
        if char in cifra:
            texto_cifrado += cifra[char]
        else:
            texto_cifrado += char
    
    return texto_cifrado


texto = input("Digite o texto  que deseja criptografar: ")

cifra = gerarcifra()

texto_cifrado = criptografia(texto, cifra)
print("Texto criptografado: ", texto_cifrado)
