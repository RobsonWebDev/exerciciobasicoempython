resp = 0

while resp != 5:
    x = int(input('Digite um valor: '))
    y = int(input('Digite outro valor: '))
    resp = int(input('''Digite:
    [1] Somar 
    [2] Multiplicar 
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programa
    '''))

    if resp == 1:
        z = x + y
        print('A Somar entre {} e {} é {}' .format(x, y, z))

    if resp == 2:
        m = x * y
        print('O produto entre {} e {} é {}' .format(x, y, m))

    if resp == 3:
        if x > y:
            print(' O maior ente {} e {} é {}' .format(x,y,x))
        elif y > x:
            print('O maior entre {} e {} é {}' .format(x,y,y))
        else:
            print('Eles sao Iguais!')

    if resp == 4:
        continue