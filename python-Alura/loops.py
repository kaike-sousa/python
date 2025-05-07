#Enquanto o número digitado for menor ou igual a zero, o programa continuará pedindo ao usuário que insira um número positivo. Quando o usuário finalmente fornecer um número positivo, o loop while será encerrado e o programa exibirá o número digitado.
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)