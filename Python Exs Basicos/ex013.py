import math
ang = float(input('Digite um angulo qualquer. '))

x = math.cos(math.radians(ang))
y = math.sin(math.radians(ang))
z = math.tan(math.radians(ang))

print('O Cosseno de {} é {:.2f}' .format(ang, x))
print('O Seno de {} é {:.2f}' .format(ang, y))
print('A Tangete de {} é {:.2f}' .format(ang, z))