numero = float(input('Digite o número que deseja realizar o calculo: '))
print ('Opções disponiveis: ')
print('1 - dobro')
print('2 - metade do número')
print('3 - 10% do valor') 
opcao = int(input('Digite a opção que deseja: '))

match opcao:
    case 1:
        dobro = (opcao * 2)
        print (f'O dobro do valor é {dobro}')

    case 2:
        divisao = (opcao / 2)
        print (f'A metade do valor é {divisao}')

    case 3:
        porcentagem = (opcao * 0.10)
        print (f'10% do valor é {porcentagem}')
