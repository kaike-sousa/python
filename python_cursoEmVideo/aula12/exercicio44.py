# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

print('Loja do kaike')
valor = float(input('Insira o valor que será pago: '))
print ('Escolha a forma de pagamento')
print ('Opção 1: À vista dinheiro/cheque: 10% de desconto')
print ('Opção 2: À vista no cartão: 5% de desconto')
print ('Opção 3: Em até 2x no cartão: preço formal')
print ('Opção 4: 3x ou mais no cartão: 20% de juros')
opcao = input('Escolha a opção desejada: ').lower()

desconto1 = valor * (10/100)
desconto2 = valor * (5/100)
desconto3 = valor * (20/100)

opcao1 = valor - desconto1
opcao2 = valor - desconto2
opcao3 = valor + desconto3

if opcao in ['opcao 1', 'opção 1', '1']:
    print (f'O valor final foi {opcao1}')
elif opcao in ['opcao 2', 'opção 2', '2']: 
    print (f'O valor final foi {opcao2}')
elif opcao in ['opcao 3', 'opção 3', '3']: 
    print (f'O valor final foi {valor}')
elif opcao in ['opcao 4', 'opção 4', '4']:
    print (f'O valor final foi {opcao3}')
else:
    print('Opção inválida!')