#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Inicialização de variáveis
soma_idade = 0
mais_velho = 0
nome_mais_velho = ""
mulheres_menos_20 = 0

for c in range(4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    
    soma_idade += idade
    
    if sexo == "M" and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
        
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

# Exibe os resultados
print(f"A média de idade do grupo é {media_idade:.2f}")
print(f"O homem mais velho é {nome_mais_velho} com {mais_velho} anos.")
print(f"Existem {mulheres_menos_20} mulheres com menos de 20 anos.")

    
