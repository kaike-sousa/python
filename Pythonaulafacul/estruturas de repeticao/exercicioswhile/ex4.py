#Faça um algoritmo que solicite N numero e calcule a media dos numeros pares e a media dos numeros impares ) o valor N deve ser solicitado no inicio do programa
numero = int(input('Digite o número de loops: '))
cont_loops = 1

contapares = 0 
contaimpares = 0 

somapares = 0
somaimpares = 0 


while cont_loops <= numero:
    numero1 = int(input('Digite um número: '))
    if numero % 2 == 0:
        somapares += numero
        contapares += 1
    else:
        somaimpares += numero
        contaimpares += 1
    cont += 1

if contapares > 0:
    print(f'Média dos pares: {somapares/ contapares}')
else:
    print(f'Não foi digitado número pares')

if contaimpares > 0:
    print(f'Média dos impares: {somaimpares/contaimpares}')
else:
    print(f'Não foi digitado números impares')
