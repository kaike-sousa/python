#Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela. Se o número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo.


valor= int(input('Por favor digite um número inteiro: '))
print(f'O número escolhido foi {valor}')

if valor < 0:
    print(f'O equivalente positivo é {valor * -1}')
else:
    print(f'O valor é {valor}')