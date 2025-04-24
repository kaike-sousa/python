
#Faça um algoritmo que solicita ao usuário uma letra e exiba uma mensagem informando se é uma vogal ou uma consoante.

letra = input('Digite uma letra: ')
vogais = ('aeiouAEIOU')

if letra in vogais:
    print('Está letra é uma vogal')
else:
    print('Esta letra é uma consoante')