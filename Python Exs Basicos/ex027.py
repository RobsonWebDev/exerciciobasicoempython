preco = int(input('Digite quanto voce ganha por hora. '))
dia = int(input('Quantas horas voce trabalha por dia. '))
sem = dia * 6

sal_bru = sem * preco * 4
imp_rend = sal_bru * 11/100
inss = sal_bru * 8/100
sind = sal_bru * 5/100

sal_liq = sal_bru - imp_rend - inss - sind

print(""" Seu Salario bruto é {} e voce paga ao INSS {}
e de IMPOSTO DE RENDA {} e paga ao SINDICATO {}
ficando um Salario Liquido de {}""" .format(sal_bru, inss, imp_rend, sind, sal_liq))
