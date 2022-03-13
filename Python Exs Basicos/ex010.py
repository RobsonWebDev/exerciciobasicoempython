alugdecarro = int(input('Quantos dias você ficou com o carro. '))
kmdocarro = float(input('Quanto quilomeetros você rodou com o carro. '))

pgdia = alugdecarro * 60
pgkm = kmdocarro * 0.15

vt = pgdia + pgkm

print('Você rodou {} dias e pagara {} pelos dias' .format(alugdecarro, pgdia))
print('Você rodou {} quilometros e pagara {} pela quilomentragem' .format(kmdocarro, pgkm))
print('Totalizando {} que você pagara pelo aluguel do carro' .format(vt))