print ('Simulador de computador de bordo')
distancia = float(input('Informe curso distância percorrida: '))
tempo = float(input('Informe o tempo da viagem: '))
#float é para numeros decimais
velocidadeMedia = distancia / tempo

print (f'A velocidade média é {velocidadeMedia:.2f}')
#f = formatação
# :.2f = número de caracteres que vai ser mostrado