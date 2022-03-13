import time

while True:
    n = int(input('Digite um umero para saber sua Tabuada: '))
    print('Calculando...')
    for c in range(1, 11):
        m = n * c
        print('{} x {} = {}' .format(n, c, m))
        time.sleep(1)

    cond = input('Deseja Continuar. [S/N]').upper()

    if cond == 'N':
        break
