#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

print('---MÉDIA ATINGIDA---')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
notafinal = (nota1 + nota2) / 2

if notafinal < 5.0:
    print ('Reprovado!')
elif  5.0 <= notafinal <= 6.9:
    print('Recuperação')
else:
    print('Aprovado!')