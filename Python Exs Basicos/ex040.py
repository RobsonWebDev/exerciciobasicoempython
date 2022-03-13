num = int(input(' Digite um numero: '))
tot = 0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[33m', end=' > ')
        tot += 1
    else:
        print('\033[31m', end=" > ")
    print('{}' .format(x))

print('Ele foi divisivel {} vezes' .format(tot))