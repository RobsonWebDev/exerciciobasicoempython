import random

cpu = random.randint(1, 5)

User = int(input('Em qual numero estou pensando entre 1 e 5. '))

if cpu == User:
    print('Nossa pensei no numero {} e vc acertou na mosca!' .format(cpu))

else:
    print('Você errou pensei no numero {} e nao no {}.' .format(cpu, User))