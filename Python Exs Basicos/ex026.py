import random

local = random.randint(100, 300)

if local > 200:

    d = local * 0.45

    print('Sua viagem é de {}km e custara {:.2f}reais' .format(local, d))

else:

    dm = local * 0.50

    print('Sua viagem é de {}km e ela custara {:.2f} reais' .format(local, dm))