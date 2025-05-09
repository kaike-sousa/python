#Vai de 1 até 9
c = 1 #começa com 1
while c < 10: #enquanto o c for menor que 10
    print(c) #vai printar o c
    c = c + 1 #vai somar o c (dessa forma inclui o 1)
print ('FIM!')

#quando usar tal numero o código irá parar
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

#mostrar números pares e impares enquanto n apertar 0 
n = 1
par = impar = 0 
while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else: 
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} numeros impares')