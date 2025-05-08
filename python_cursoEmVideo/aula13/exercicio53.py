#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase: ").strip().upper()
frase_sem_espaco = frase.replace(" ", "")

# Inverte a frase
frase_invertida = frase_sem_espaco[::-1]

# Verifica se é igual à frase original sem espaços
if frase_sem_espaco == frase_invertida:
    print("A frase É um palíndromo!")
else:
    print("A frase NÃO é um palíndromo.")
