import random

esc = random.randint(1, 5)
print(' O numero foi {}' .format(esc))

if esc == 1:
    print('Yasmin, voce foi escolhida')

elif esc == 2:
    print('Matheus, voce foi escolhido')

elif esc == 3:
    print('Moises, vc foi escolhido')

elif esc == 4:
    print('Levi, voce foi escolhido')

else:
    print('Ninguem foi escolhido!')