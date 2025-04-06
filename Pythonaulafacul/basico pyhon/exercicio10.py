numero = int(input('informe um número inteiro de três digitos: '))

a = numero // 100
resto = numero % 100

b = resto // 10
c = resto % 10

print(f'Numero invertido {c}{b}{a}')
