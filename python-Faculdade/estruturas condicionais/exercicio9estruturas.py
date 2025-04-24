#9. Faça um algoritmo que solicita ao usuário três valores correspondentes aos lados de um triângulo. Informe se o triângulo é equilátero (possui 3 lados iguais), isósceles (possui dois lados iguais) ou escaleno (não possui lados iguais).


numero1 = float(input('Insira o primeiro número do triângulo: '))
numero2= float(input('Insira o segundo número do triângulo: '))
numero3 = float(input('Insira o terceiro número do triângulo: '))

if numero1 == numero2 and numero1 == numero3 and numero2 == numero3:
    print(f'É um triângulo equilátero')
elif numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    print(f'É um triângulo isósceles')
else:
    print('É um triângulo escaleno')
