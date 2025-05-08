#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Bem vindo ao empréstimo bancário para a compra de sua casa')
valorCasa = float(input('Por favor digite o valor da casa desejada: R$'))
salario = float(input('Por favor digite o seu salário: R$'))
tempo = int(input('Por favor digite o tempo em que deseja pagar: '))
prestacao = valorCasa / (tempo * 12)
minimo = salario * 30 / 100
if prestacao > minimo: 
    print (f'Empréstimo negado, pois o seu salário é {salario:.2f} e o valor da prestação é {prestacao:.2f}')
else:
    print (f'Empréstimo aceito, pois o seu salário é {salario:.2f} e o valor da prestação é {prestacao:.2f}')