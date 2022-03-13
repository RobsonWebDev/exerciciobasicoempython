atleta = int(input('Ano de nascimento do atleta: '))

idade_atual = 2022 - atleta

if idade_atual <= 9:
    print('Você vai competir na categoria MIRIM')

elif idade_atual >= 10 and idade_atual <= 14:
    print('Você vai competir na categoria INFANTIL')

elif idade_atual >= 15 and idade_atual <= 19:
    print('Você ira competir na categoria JUNIOR')

elif idade_atual == 20:
    print('Você ira competir na categoria SENIOR')

else:
    print('Você ira competir na categoria MASTER')