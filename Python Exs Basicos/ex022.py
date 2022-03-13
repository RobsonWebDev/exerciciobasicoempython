nome =  str(input('Digite seu nome.  ')).strip()
nm = nome.split()

print('Seu primeiro nome é {}' .format(nm[0]))
print('Seu ultimo nome é {}' .format(nm[len(nm)-1]))