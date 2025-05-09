#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
'''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))


opcao = 0
while opcao != 5:
    print('Escolha Novamente')
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar ')
    print('[ 3 ] maior ')
    print('[ 4 ] novos números ')
    print('[ 5 ] sair do programa ')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        soma = numero1 + numero2
        print(f'O resultado da soma é {soma}')
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print(f'O resultado da multiplicação é {multiplicacao}')
    elif opcao == 3:
        if numero1 > numero2:
            print ('O maior foi o primeiro número')
        else:
            print('O segundo foi o maior número')
    elif opcao == 4:
        print('Informe os números novamente: ')
        numero1 = int (input('Digite o primeiro número: '))
        numero2 = int (input('Digite o segundo número: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('Opção Inválida')
print('Fim do programa')



