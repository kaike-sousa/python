#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for c in range (termo, decimo + razao, razao):
    print (c)
print('Acabou!')
