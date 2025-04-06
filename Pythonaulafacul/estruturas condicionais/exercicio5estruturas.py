#Faça um algoritmo que solicita um número inteiro e exibe uma mensagem indicando se ele é positivo, negativo ou zero

numero = int(input('Digite um número inteiro: '))
if numero == 0 :
    print('O número digitado é zero')
elif numero > 0 :
    print('O número digitado é positivo')
elif numero < 0 :
    print('O número é negativo')