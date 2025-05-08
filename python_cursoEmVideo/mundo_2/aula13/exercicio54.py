# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
pessoasMenor = 0
pessoasMaior = 0

for c in range (0, 7):
    anoNascimento = int(input('Informe o ano de seu nascimento: '))
    if (ano_atual - anoNascimento) <18: 
        pessoasMenor += 1
    else:
        pessoasMaior += 1
print(f' A quantidade de pessoas menor de idade é {pessoasMenor} e a quantidade de pessoas maior de idade é {pessoasMaior}')

