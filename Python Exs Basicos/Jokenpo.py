import random

while True:

    jogador = int(input('Escolha [1] para Pedra [2] para Tesoura ou [3] para Papel: '))

    jogada1 = 'Pedra'
    jogada2 = 'Tesoura'
    jogada3 = 'Papel'

    jokenpo = ['Pedra', 'Papel', 'Tesoura']

    cpu = random.choice(jokenpo)

    if jogador == 1:

        print('-=' * 20)
        print(jogada1)
        print('x' * 20)
        print(cpu)
        print('-=' * 20)
        
        if cpu == jogada1:

            print('-=' * 20)
            print('Jogamos Iguais, Ninguem Ganhou!')
            print('-=' * 20)

        elif cpu == 'Papel':

            print('-=' * 20)
            print('Ganhei e voce Perdeu!')
            print('-=' * 20)

        else:

            print('-=' * 20)
            print('Parabens voce ganhou')
            print('-=' * 20)

    elif jogador == 2:

        print('-=' * 20)
        print(jogada2)
        print('x' * 20)
        print(cpu)
        print('-=' * 20)

        if cpu == jogada2:

            print('-=' * 20)
            print('Jogamos Iguais, Ninguem Ganhou!')
            print('-=' * 20)

        elif cpu == 'Pedra':

            print('-=' * 20)
            print('Ganhei e voce Perdeu!')
            print('-=' * 20)

        else:

            print('-=' * 20)
            print('Parabens voce ganhou')
            print('-=' * 20)

    elif jogador == 3:

        print('-=' * 20)
        print(jogada3)
        print('x' * 20)
        print(cpu)
        print('-=' * 20)

        if cpu == jogada3:

            print('-=' * 20)
            print('Jogamos Iguais, Ninguem Ganhou!')
            print('-=' * 20)

        elif cpu == 'Tesoura':

            print('-=' * 20)
            print('Ganhei e voce Perdeu!')
            print('-=' * 20)

        else:

            print('-=' * 20)
            print('Parabens voce ganhou')
            print('-=' * 20)

    else:
        print("Digite um numero valido entre 1 e 3")