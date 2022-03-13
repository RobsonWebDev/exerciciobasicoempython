frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palindromo')
else:
    print('Nao temos um Palidromo')


'''
frases para testar

Apos a Sopa
A Sacada da Casa
A Torre da Derrota
O Lobo ama o bolo
Anotaram a data da maratona

'''