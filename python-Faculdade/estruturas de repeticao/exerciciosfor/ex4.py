#Escreva um algoritmo que exiba 20 números aleatórios sorteados entre 1 e 50 (Dica: importe abiblioteca random)
import random

for numeros in range(20):
    aleatorio = random.randint(0, 50)
    print(aleatorio)
    
    