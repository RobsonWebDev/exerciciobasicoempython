import random

#jogo de PAR ou IMPAR

contplay = contcpu = 0
while True:
    n = int(input('Digite Um numero de 1 a 10: '))
    esc = input('Escolha [P]ar ou [I]mpar: ').upper()
    cpu = random.randint(1, 11)
    print('CPU: Eu escolhi {}' .format(cpu))
    s = n + cpu
    if esc == 'P':
        if s % 2 == 0:
            print('Deu Par vc Ganhou')
            contplay += 1
        else:
            print(' Deu Impar, Você Perdeu!!')
            contcpu += 1
            break

    elif esc == 'I':
        if s % 2 == 0:
            print('Deu Par vc Perdeu!!')
            contcpu += 1
            break
        else:
            print('Deu Impar, Você Ganhou!!')
            contplay += 1

    else:
        print('Digite [P/I]: ')

print('O Você fez {} ponto(s) e a CPU fez {} ponto(s)' .format(contplay, contcpu))