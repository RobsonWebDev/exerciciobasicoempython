contM = 0
contm = 0
for i in range(0, 7):
    nasci= int(input('Digite o seu nascimento: '))
    idade = 2022 - nasci

    if idade > 18:
        contM += 1
        print('Que Legal vc é maior de Idade')

    else:
        contm += 1
        print('Que pena vc ainda nao é de maior.')

print('{} pessoas sao maiores de idade e {} nao sao' .format(contM, contm))