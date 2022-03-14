import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP', ip)
        print('~=' * 35)
        os.system('ping -n 2 {}'.format(ip))
        print('~=' * 35)
        time.sleep(5)