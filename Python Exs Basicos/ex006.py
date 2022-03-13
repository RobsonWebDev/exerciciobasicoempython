while True:

    x = input('Se você quiser converter de Real para Dolar aperte [d] se for de dolar para o real aperte[r] ')

    if x == 'd':
        valor = float(input('Me diga quanto você tem em Real. '))

        d = valor / 5

        print(f'Você recebera {d} dolares')
                
    elif x == 'r':
        real = float(input('Me diga quanto vc tem em Dolares. '))

        r = real * 5

        print(f'Você recebera {r} reias')

    else:
        print('por favor digite [d] ou [r]')

