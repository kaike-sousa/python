#Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada de cada número (Dica: importe a biblioteca math).

import math

print('Informe 15 números: ')

for numero in range (1, 15):
    insira = int(input())
    raiz_quadrada = math.sqrt(insira)
    print(raiz_quadrada)
