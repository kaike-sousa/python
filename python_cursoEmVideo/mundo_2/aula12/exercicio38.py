#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))

if numero1 > numero2:
    print ('O maior número é o primeiro')
elif numero1 == numero2:
    print('Os números são iguais')
else:
    print('O segundo número é maior')