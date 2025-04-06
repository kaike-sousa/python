n = input('Por favor senhor informe o seu nome completo: ')
carrosVendido = int(input('Por favor informe o número de carros vendidos: '))
valorDeVendas = float(input('Por favor informe o valor total de vendas: '))

valorfinal = 2500 + (carrosVendido * 200.00) + (valorDeVendas * 0.02 )

print ('Nome do vendedor: ' + n)
print (f'Quantidade de carros vendidos: {carrosVendido}')
print (f'Valor total das vendas: {valorDeVendas}')
print (f'O vendedor Paulo receberá um salário de R$ {valorfinal:.2f}')