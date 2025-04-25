#Escreva um algoritmo que determine se um número N (informado pelo usuário) é primo ou não

numero = int(input('Digite um número: '))
conta_divisores = 0 

for n in range(1, numero+1):
    if numero % n == 0 :
        conta_divisores += 1

if conta_divisores == 2:
    print(f'É um número primo, {numero}')
else:
    print(f'Não é um número primo, {numero}')
