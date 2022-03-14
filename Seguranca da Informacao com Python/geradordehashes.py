import hashlib


string = input('Digite o texto a ser codificado. ')

menu = int(input('''
### Menu - Escolha o tipo de Hash ###
[1] MD5
[2] SHA1
[3] SHA256
[4] SHA512
[5] SAIR
Digite o numero da Hash a ser gerado: 
'''))


if menu == 1:

    resultado = hashlib.md5(string.encode('utf-8'))

    print('O hash MD5 da string', string,' é: ', resultado.hexdigest())

elif menu == 2:

    resultado = hashlib.sha1(string.encode('utf-8'))

    print('O hash MD5 da string', string,' é: ', resultado.hexdigest())

elif menu == 3:

    resultado = hashlib.sha256(string.encode('utf-8'))

    print('O hash MD5 da string', string,' é: ', resultado.hexdigest())

elif menu == 4:

    resultado = hashlib.sha512(string.encode('utf-8'))

    print('O hash MD5 da string', string,' é: ', resultado.hexdigest())
