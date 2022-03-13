cont = 0
password ='Yes=123'
for login in range(99):
    user = str(input('Digite seu usuario: '))
    senha = str(input('Digite seu Password: '))

    if user == senha:
        cont += 1
        print('sua Senha nao pode ser igual ao seu Usuario!')
        if cont >= 3:
            print('Usuario Bloqueado Redefina sua Senha!')

    elif senha == password:
        print('Acesso Lliberado!')

    else:
        cont += 1
        if cont >= 3:
            print('Usuario Bloqueado Redefina sua Senha')
        print('Digite um password valido!')