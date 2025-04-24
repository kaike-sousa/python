# Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
salario = float(input('Por favor digite o seu salário fixo: '))
vendas = float(input('Por favor digite o valor das vendas efetuadas: '))

if vendas <= 1500:
    comissao = vendas * 0.03
    total = salario + comissao
    print(f'O salário será {vendas}')
else:
    comissao1 = 1500 * 0.03
    comissao2 = (vendas - 1500) * 0.05
    total = salario + comissao1 + comissao2

print(f'O seu salário será de R${total:.2f}')