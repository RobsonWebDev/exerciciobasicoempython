primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 -1) * razao

for x in range(primeiro, decimo + razao, razao):
    print('{}' .format(x), end=' >> ')
print('Acabou!')