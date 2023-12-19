import random
import math

def eh_primo(numero):
    if numero<2:
        return False
    for i in range(2,numero//2+1):
        if numero%i == 0 :
            return False
    return True

def gera_primo(minimo,maximo):
    primo = random.randint(minimo,maximo)
    while not eh_primo(primo):
        primo = random.randint(minimo,maximo)
    return primo  

def mod_inverso(e,phi):
    for d in range(3,phi):
        if (d*e) % phi == 1:
            return d
    raise ValueError("mod inverso nao existe")

def criptografar(mensagem,e,n):
    convertida = [ord(caracter) for caracter in mensagem]
    #(m^e) mod n = c
    criptograma = [pow(caracter,e,n) for caracter in convertida]
    return criptograma

def decriptografar(criptograma,d,n):
    convertida = [pow(caracter,d,n) for caracter in criptograma]
    mensagem = "".join(chr(caracter) for caracter in convertida)
    return mensagem

p, q = gera_primo(1000, 5000), gera_primo ( 1000, 5000)
while p==q:
    q= gera_primo(1000, 5000)

n = p * q
#Funcao totiente de Euler
phi_n = (p-1) * (q-1)

e = random.randint (3, phi_n-1)
while math.gcd(e, phi_n) != 1: #gcd=greater common denometer ou MDC em portugues
     e = random.randint (3, phi_n - 1)

d = mod_inverso(e, phi_n)

mensagem = "Attack at dawn"
print(f"Mensagem original: {mensagem}")
criptograma = criptografar(mensagem,e,n)
print(f"Mensagem criptografada: {criptograma}")
print(f"Mensagem decriptografada: {decriptografar(criptograma,d,n)}")