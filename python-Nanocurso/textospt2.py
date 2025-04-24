from html.parser import commentclose

texto = 'esse texto quebra curso linha \n aqui. E para fazer uma \t tabulação'
print(texto)

texto = 'texto em letras maisculuas'
print(texto.upper())
#para deixar todas as letras do texto maiusculas

texto = 'LETRAS MINISCULAS'
print(texto.lower())
#para deixar todas as letras do texto minusculas

print(texto.startswith('LET'))
# serve para falar se algo é verdadeiro ou falso, logica booleana, neste caso perguntando se o texto COMEÇA com LET, no caso é true

print(texto.endswith('!'))
# serve para falar se algo é verdadeiro ou falso, logica booleana, neste caso perguntando se o texto TERMINA com !, no caso é false

print(texto.count('@'))
#serve para perguntar quantos @ tem dentro do texto

print('MINISCULAS' in texto)
#perguntando se tem curso palavra minuscula dentro do texto

