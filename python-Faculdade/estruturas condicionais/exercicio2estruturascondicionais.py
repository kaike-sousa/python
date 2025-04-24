#Faça um algoritmo que solicita ao usuário um valor inteiro e exibe uma mensagem informando se o número é par ou ímpar.

valor= int(input('Por favor digite um número inteiro: '))
if valor % 2 == 0:
    print('O número é par!')
else:
    print("O número é impar!")