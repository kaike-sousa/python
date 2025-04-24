#Faça um algoritmo que solicita ao usuário dois números inteiros. O primeiro é o valor das horas e o segundo dos minutos. Verifique se a hora é válida ou inválida e exiba uma mensagem correspondente (São válidas as horas entre 00:00 e 23:59).

horas = int(input('Digite um número inteiro entre 0 e 24: '))
minutos = int(input('Digite um segundo número entre 0 e 60: '))

if horas >= 0 and horas < 24 and minutos >= 0 and minutos < 60:
    print(f'O número é {horas:02}:{minutos:02} é valido')
else:
    print(f'O número é inválido')
