import random

contplay = 0
contcpu = 0
resp = ''

while resp != 'n':

    game = int(input('Em qual numero estou pensando. '))
    x = random.randint(1, 10)

    if game == x:
        contplay += 1
        print('Parabens Voce digitou {} e eu pensei em {} voce ganhou.' .format(game, x))

    if game != x:
        contcpu += 1
        print('Hahahaha!!! voce perdeu, {} foi o numero que pensei e voce digitou {}' .format(x, game))

    resp = str(input('Deseja continua [S/N]'))

    print('Jogador tem {} pontos' .format(contplay))
    print('A CPU tem {} pontos' .format(contcpu))