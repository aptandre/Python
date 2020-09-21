cadastros = []
while True:
    print('-'*20)
    user = int(input('Digite o que deseja fazer: \n1 - Listar cadastros \n2- Cadastrar alguém \n3- Sair do sistema. \n'))
    print('-'*20)
    pleural = []
    if user == 1:
        try:
            with open('arquivo.txt', 'r') as arc:
                adastros = arc.read()
                pleural.append(adastros)
                for elemento in pleural:
                    print(elemento[0], end='     ')
                    print(elemento[1])
        except IndexError:
            print('Lista de cadastrados vazia.')
    elif user == 2:
        with open('arquivo.txt', 'a') as arq:
            nome = input('Digite o nome da pessoa: ')
            idade = input('Digite a idade da pessoa: ')
            #cadastros.append(nome)
            #cadastros.append(idade)
            arq.write(f'[{nome}, {idade}],')
            cadastros.clear()
    elif user == 3:
        print('Obrigado, volte sempre.')
        break

'''lista = [['André', '17'],['Sakura', '15']]
for elemento in lista:
    print(elemento[0], end='     ')
    print(elemento[1])'''