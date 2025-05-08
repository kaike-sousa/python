#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

print ('Calculo de Índice de Massa Corporal (IMC)')
peso = float(input('Digite o seu peso: (kg)'))
altura = float(input('Digite a sua altura: (m) '))
imc= peso / altura ** 2

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print ('Abaixo do peso')
elif 18.5 <= imc < 25.0:
    print ('Peso ideal')
elif 25.0 <= imc < 30.0:
    print ('Sobrepeso')
elif 30.0 <= imc < 40.0:
    print ('Obesidade')
else: 
    print ('Obesidade Mórbida')