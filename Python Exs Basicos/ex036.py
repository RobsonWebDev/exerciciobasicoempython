s = 0
cont = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        s = s + x
        cont += 1
        print(x)
print(cont)
print(s)