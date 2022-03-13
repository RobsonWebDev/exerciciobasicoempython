a = float(input('Digite sua media da I Unidade. '))

b = float(input('Digite sua media da II Unidade. '))

c = float(input('Digite sua media da III Unidade. '))

d = float(input('Digite sua media da IV Unidade. '))

m = (a + b + c + d) / 4

print(f'Suas notas foram {a, b, c, d} e a sua media aritmetica foi {m}')

if m == 7:
    print('Ufa! você passou arrastado, se dedique mais nos estudos.')

elif m >= 7:
    print('Parabéns você foi aprovado!')

else:
    print('Ahh que pena!! você nao conseguiu obter a media ideal')
