nascimento = int(input('Em qual ano você nasceu: '))

idade_atual = 2022 - nascimento
ano_atras = idade_atual - 18
ano_de_alista1 = 2022 - ano_atras
ano_pra_frente = 18 - idade_atual
ano_de_alista2 = 2022 + ano_pra_frente

if idade_atual == 18:

    print('Esse ano você tera que se alistar.')

elif idade_atual > 18:

    print('Você deveria te se alistado no ano de {} ha {} atrás' .format(ano_de_alista1, ano_atras))

else:

    print('Voce so vai poder se alistar em {} daqui a {} anos' .format(ano_de_alista2, ano_pra_frente))