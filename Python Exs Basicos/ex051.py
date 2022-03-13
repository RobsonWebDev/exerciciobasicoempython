contprod = contprec = 0

while True:
    prod = input('Nome do Produto: ')
    prec = float(input('Preço do Produto: '))
    contprod += 1
    if prec >= 1000:
        contprec += 1

    totalgasto = contprod * prec

    if contprod == 1:
        menor = prec
        barato = prod

    else:
        if prec < menor:
            menor = prec
            barato = prod

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar. [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Voce comprou {contprod} produto(s)')
print(f'Sua conta deu um total de R$: {totalgasto:.2f}')
print(f'{contprec} dos seus produtos custarao mais de R$1000')
print(f'O {barato.upper()} custa {menor:.2f} e é o produto mais barato da sua lista')