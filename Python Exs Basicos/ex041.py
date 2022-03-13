somaidade = 0
mediaidade = 0
maioridadedohomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('-=-=- {}pessoa -=-=-' .format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedohomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadedohomem:
        maioridadedohomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1

mediaidade = somaidade / 4


print('A media de idade do grupo é {}' .format(mediaidade))
print('O homem mais velho tem {} e se chama {}.' .format(maioridadedohomem, nomevelho))
print(' Ao todo sao {} mulheres com menos de 20 anos.' .format(totmulher20))