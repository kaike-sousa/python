#Faça um algoritmo que solicite dois números ao usuário e exiba apenas o maior deles. Caso eles sejam iguais exiba a mensagem “Números Iguais”.


numero1 = float(input('Insira o primeiro número: '))
numero2= float(input('Insira o segundo número: '))

if numero1 == numero2:
    print(f'Os números são iguais {numero1} = {numero2}')
elif numero1 > numero2:
    print(f'O número 1 ({numero1}) é maior que o número 2 ({numero2})')
elif numero1 < numero2:
    print(f'O número 2 ({numero2}) é maior que o número 1 ({numero1})')