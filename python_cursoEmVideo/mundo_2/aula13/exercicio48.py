#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont= 0
for c in range(1, 501, 2):
    if c % 3 == 0: # é múltiplo de 3
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} valores é {soma}')


#Exercicio para praticar
#Faça um programa que mostre a soma de todos os números pares múltiplos de 4 que estão no intervalo de 1 até 600. Ao final, mostre quantos números foram somados.
soma = 0
quant = 0 
for c in range(0, 601, 2):
    if c % 4 == 0:
        quant = quant + 1
        soma = soma + c
print(f'O resultado dos {quant} números de 1 até 600 que são números pares múltiplos de 4 é equivalente à {soma}')
