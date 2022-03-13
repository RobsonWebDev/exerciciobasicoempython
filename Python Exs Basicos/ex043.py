contm = 0
contf = 0
resp1 = ''
while resp1 != 'n':

    resp = str(input('Digite seu sexo com [M] Masculino e [F] Feminino: '))

    if resp == 'm':
        contm += 1


    elif resp == 'f':
        contf += 1

    else:
        print('Digite um valor valido!')

    resp1 = str(input('Deseja Continuar [S/N]: '))

    print('Sao {} homens e {} mulheres no sistema' .format(contm, contf))