casa = float(input('Qual o valor da casa: '))
salario = float(input('De quanto é seu salario: '))
promissoria = int(input('Em quanto anos vc pretende quitar a casa: '))

x = salario * 30/100
a = promissoria * 12
y = casa / a

if y <= x:
    
    print('''Parabéns! Seu Emprestimo para aquisicao da casa foi Aprovado.
    e suas parcelas ficou de {:.2f} em {} vezes.''' . format(y, a))
    
else:

    print('Infelizmente nao foi dessa vez! Seu pedido foi Negado.')