num = int(input('Digite um numero para saber sua Tabuada: '))

for x in range(1, 11):
    m = num * x

    print('{} * {} = {}' .format(num, x, m))