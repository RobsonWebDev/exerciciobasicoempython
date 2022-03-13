x = float(input('Qual o valor do cateto oposto. '))
y = float(input('Qual o valor do cateto adjacente. '))
z = (y**2 + x**2)**(1/2)

print('Seu Cateto Oposto mede {} e seu Cateto Adjacente mede {} e sua Hipotenusa é igual a {:.2f}' .format(x, y, z))