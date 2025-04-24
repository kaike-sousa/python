media= float(input('Digite a média: '))
faltas= int(input('Qual foi a quantidade de faltas: '))

if media >= 6 and faltas <= 20:
        print('Aprovado')
elif media >= 6 and faltas >20:
    print ('Reprovado por faltas')
else:
    print('Reprovado por media')