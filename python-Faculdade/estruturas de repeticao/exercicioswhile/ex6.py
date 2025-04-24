#ESCREVA UM ALGORITMO QUE SOLICITE 10 NUMEROS E INFORME QUAL FOI O MENOR NUMERO DIGITADO
cont = 1
menor = 0

while cont <= 10:
    n = int(input('Digite o número: '))
    if menor == 0:
        n = menor
    if n < menor:
        menor = n
    cont += 1

print(f'O menor número digitado foi {menor}')
