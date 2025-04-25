#Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.
print('Insira 10 números inteiros')  # Exibe uma mensagem pro usuário

for i in range(10):  # Laço que repete 10 vezes
    num = int(input(f'Digite o número: '))  # Lê o número digitado e converte pra inteiro

    if i == 0:  # Se for o primeiro número digitado
        menor = num  # Define o menor como esse número
        maior = num  # Define o maior como esse número
    else:
        if num > maior:  # Se for maior que o atual 'maior'
            maior = num  # Atualiza o maior
        if num < menor:  # Se for menor que o atual 'menor'
            menor = num  # Atualiza o menor

print(f'O maior número é {maior}')  # Exibe o maior número encontrado
print(f'O menor número é {menor}')  # Exibe o menor número encontrado
