#SOLICITA IDADE 10 PESSOAS e informar a quantidade de pessoas menor de 18
cont = 1
idade_menor = 0 

while cont <= 10:
    idade = int(input('Digite a idade: '))
    if idade < 18:
        idade_menor += 1
    cont += 1
print (f'Pessoas menor de 18: {idade_menor}')