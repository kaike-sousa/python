#Faça um algoritmo que solicita ao usuário as notas de três provas. Calcule a média aritmética e informe se o aluno foi Aprovado ou Reprovado (o aluno é considerado aprovado com a média igual ou superior a 6).

notaA = float(input('Digite a primeira nota: '))
notaB = float(input('Digite a segunda nota: '))
notaC = float(input('Digite a terceira nota: '))

mediaAritmetica= (notaA + notaB + notaC) / 3
print(f'A sua media foi {mediaAritmetica}')
if mediaAritmetica >= 6 :
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')