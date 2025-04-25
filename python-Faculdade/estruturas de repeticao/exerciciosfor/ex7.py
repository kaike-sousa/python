# Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.

solicitacao = int(input('Digite um número inteiro: '))

for divisores in range(1, solicitacao +1):
    if solicitacao % divisores == 0:
        print(divisores)
