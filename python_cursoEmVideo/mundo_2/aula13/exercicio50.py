#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma_pares = 0 
for numero in range(0, 6):
    numero = int((input('Digite o número inteiro: ')))
    if numero % 2 == 0:
        soma_pares = soma_pares + numero
print(f'A soma dos números pares é {soma_pares}')
