#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('Alistamento Militar')
from datetime import date

print('=== Alistamento Militar ===')
ano_nasc = int(input('Informe o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade == 18:
    print('Está na hora exata de se alistar!')
elif idade > 18:
    passou = idade - 18
    print(f'Já passou o tempo de se alistar. Você deveria ter se alistado há {passou} ano{"s" if passou > 1 else ""}.')
else:
    falta = 18 - idade
    print(f'Ainda não é a hora exata de se alistar. Faltam {falta} ano{"s" if falta > 1 else ""} para o alistamento.')
