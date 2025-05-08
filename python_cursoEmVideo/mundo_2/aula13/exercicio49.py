#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#DIGITAR UM NUMERO PARA VER A TABUADA DELE DE 1 À 10

numero = int(input('Digite o número que deseja ver a tabuada: '))
for tabuada in range (1, 11):
    print (f'{numero} x {tabuada} = {numero * tabuada}')