s = 0
c = 0
for x in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 ==0:
        s += num
        c += 1

print('Voce digitou {} numero e a soma foi {}.' .format(c, s))