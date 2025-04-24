#Pedir ao usuário 5 número e ver se é par ou ímpar

contagem = 1
while contagem <= 5:
    numero = int(input('Número: '))
    if numero % 2 == 0:
        print ('par')
    else:
        print('impar')
    contagem += 1