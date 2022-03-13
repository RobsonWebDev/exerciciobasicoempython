sele = int(input('''
    Quital convertermos um numero inteiro em
    [1] Binario, [2] Octal e [3] Hexal: 
'''))

numero = int(input('Digite o valor que queira converter: '))

if sele == 1:
    
    bin = bin(numero)
    print('O numero {} em binario fica {}.' .format(numero, bin))

elif sele == 2:

    oct = oct(numero)
    print('O numero {} em octal fica {}' .format(numero, oct))

elif sele == 3:

    hex = hex(numero)
    print('O numero {} em hexadecimal fica {}' .format(numero, hex))

else:
    print('Digite apenas [1], [2] ou [3]')