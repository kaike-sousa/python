#SOLICITE DOIS NUMEROS AO USUARIO CASO OS NUMEROS SEJAM IGUAIS O ALGORITMO DEVE SOLICITAR UM NUMERO NOVAMENTE E INFORME A SOMA ENTRE OS NUMEROS


while True:
    numero1 = (int(input('Digite o primeiro número: ')))
    numero2 = (int(input('Digite o segundo número: ')))
    if numero1 != numero2:
        print(f'A soma dos números é {numero1 + numero2}')
        break
    else: 
        print('Digite números diferentes')
