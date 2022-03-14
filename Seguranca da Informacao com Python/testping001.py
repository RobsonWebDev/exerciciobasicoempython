import os

ip_ou_host = input('Digite um IP ou Host ha ser verificado: ')

os.system('ping -n 6 {}' .format(ip_ou_host))