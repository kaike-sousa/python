#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo: [M/F]  ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Tente Novamente: ')).upper()[0].strip()
print(f'Você foi aceito, sexo inserido {sexo}')

