#Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for n in range(numero, 0, -1):
    fatorial = fatorial * n  # fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}")
3