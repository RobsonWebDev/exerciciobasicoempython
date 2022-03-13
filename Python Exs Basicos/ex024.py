import random

print('Alerta! radar a frente reduza a sua velocidade.')

radar = random.randint(50, 120)

if radar > 80:
    
    vm = radar - 80
    multa = vm * 7

    print('Sua velocidade foi {} e vc excedeu o limite necessario e vai pagar {} reais de multa.' .format(radar, multa))

else:

    print('Sua velocidade foi {}km/h, dirija sempre com cuidado' .format(radar))