#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#para converter: 
#bin() → para binário
#oct() → para octal
#hex() → para hexadecimal

number = int(input('Por favor digite um número inteiro: '))
print ('Escolha uma opção')
print ('Opção 1: converter para binário')
print ('Opção 2: Converter para octal')
print ('Opção 3: Converter para hexadecimal')
opcion = input ('Digite sua opção: ') .strip().lower()
if opcion == 'opção 1' or opcion=='1' or opcion=='opcao 1':
    print (f'O número convertido para binario fica {bin(number)}')
elif opcion == 'opção 2' or opcion=='2' or opcion=='opcao 2':
    print (f'O número convertido para octal fica {oct(number)}')
elif opcion == 'opção 3' or opcion=='3' or opcion=='opcao 3':
    print (f'O número convertido para hexadecimal fica {hex(number)}')
else:
    print('Opção invalida!')
