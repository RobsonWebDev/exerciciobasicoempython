contidade = contsexoM = contsexoF = 0


while True:
    idade = int(input('Digite a sua idade. '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite [M/F] para Masculino ou Feminino. ')).strip().upper()[0]

    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        contsexoM += 1
    if sexo == 'F' and idade < 20:
        contsexoF


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar. [S/N ')).strip().upper()[0]
    if resp == 'N':
        break


print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'temos ao todo {contsexoM} homens')
print(f'temos um total de {contsexoF} mulheres com menos de 20 anos')