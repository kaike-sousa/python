# Faça um algoritmo que solicita ao usuário três números e exibe na tela apenas o menor deles, ou umamensagem informando que os números são iguais.

numero1 = float(input('Insira o primeiro número: '))
numero2= float(input('Insira o segundo número: '))
numero3 = float(input('Insira o terceiro número: '))

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
elif numero2 < numero1 and numero2 < numero3:
    print(numero2)
elif numero3 < numero1 and numero3 < numero2:
    print(numero3)
elif numero3 == numero2 and numero3 == numero1 and numero1 == numero2:
    print('Os números são iguais')



