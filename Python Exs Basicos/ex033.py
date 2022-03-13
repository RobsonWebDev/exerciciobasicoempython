produto = str('O preço do produto é de R$200')
pagamento = int(input('''Qual o metodo de pagamento
[1] á vista, [2] cartao á vista, [3] 2x no cartao, [4] acima de 3x no cartao
'''))

dinheiro = 200 - (200 * 10/100)
cartao_avista = 200 - (200 * 5/100)
credito2x = 200
credito3x = 200 + (200 * 20/100)

if pagamento == 1:
     print('Vai te custa apenas R${}' .format(dinheiro))

elif pagamento == 2:
    print('Vai te custar R${}' .format(cartao_avista))

elif pagamento == 3:
    print('Nao houve alteraçao vai te custar R${}' .format(credito2x))

elif pagamento == 4:
    print('Vai ter um acrecimo de 20% por isso custara R${}' .format(credito3x))

else:
    print('Digite apenas [1], [2], [3] ou [4]')