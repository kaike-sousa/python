"""
1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""

#Exercicio 1
''' 
numero = int(input('Insira um número: '))

if numero % 2 == 0:
    print('O número inserido é par')
else:
    print('O número inserido é impar')
'''

#Exercicio 2
idade = int(input('Insira sua idade: '))

if idade >= 0 and idade <=12:
        print('É uma criança')
elif idade >= 13 and idade <=18:
    print('É um adolescente')
elif idade >= 18:
    print('É um adulto')
else:
    print('Invalido')
