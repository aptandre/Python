username = input('Digite o seu nome de usuário: ')
senha = input('Digite a sua senha: ')
while username == senha:
    print('O nome de usuário e senha são iguais! Coloque-os de maneira mais segura:')
    username = input('Digite o seu nome de usuário: ')
    senha = input('Digite a sua senha: ')
print(f'Olá \033[0;33m{username} \033[m')