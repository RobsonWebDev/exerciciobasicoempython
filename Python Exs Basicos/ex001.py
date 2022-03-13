num1 = int(input('Digite um Numero. '))
num2 = int(input('Digite outro numero. '))
calc = input('Digite [a] para soma, [s] para subtracao, [m] para multiplicacao, [d] para divisao. ')

if calc == 'a':

    a = num1 + num2

    print(a)

elif calc == 's':

    s = num1 - num2

    print(s)

elif calc == 'm':

    m = num1 * num2

    print(m)

elif calc == 'd':

    d = num1 / num2

    print(d)

else:
    print('Operador Invalido, Por Favor digite uma das letras')
