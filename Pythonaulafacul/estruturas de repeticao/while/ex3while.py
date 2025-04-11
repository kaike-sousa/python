#solicitar a idade de 10 pessoas e calcular a media de idade
conta_idades = 0
soma_idades = 0

while True:
    idade = int(input('Informe a sua idade: '))
    if idade < 0:
        break

print(soma_idades )  
if conta_idades > 0:  
    media = soma_idades / conta_idades
    print (f'Média de idade das pessoas: {media:.2f}')
else:
    print('Nehuma idade foi informada')