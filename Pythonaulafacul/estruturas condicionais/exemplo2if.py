media= float(input('Digite a média: '))
faltas= int(input('Qual foi a quantidade de faltas: '))

if media >= 6:
    if faltas <= 20:
        print('Aprovado')
    else:
        print('Você foi reprovado por faltas!')
else:
    print('Reprovado por faltas')