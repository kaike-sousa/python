#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0 
menor = 0
for c in range (1, 6):
    peso = float(input(f'Informe o peso da {c}° pessoa: (kg) ')) 
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: 
            maior = peso
        if peso < menor: 
            menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}')


#OUTRA FORMA
maior_peso = 0
menor_peso = float('inf')  # Definimos o menor peso como infinito inicialmente

for c in range(5):
    peso = float(input(f'Informe o peso da {c + 1}ª pessoa: '))
    
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso é {maior_peso} e o menor peso é {menor_peso}')
