#Calculando quantos numeros forem necessarios
#É interroompido somente digitando o 999 que nao sera adicionado a conta

soma = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n


print(soma)