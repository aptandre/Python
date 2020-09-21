num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
load = int(input('Digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
while load > 0 and load < 5:
    if load == 1:
        print(f'A soma dos números é {num1 + num2}')
        print('=' * 20)
        load = int(input('Agora, digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
    elif load == 2:
        print(f'O produto dos números é {num1 * num2}')
        print('=' * 20)
        load = int(input('Agora, digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
    elif load == 3:
        if num1 > num2:
            print(f'O maior número deles é {num1}')
            print('=' * 20)
            load = int(input('Agora, digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
        else:
            print(f'O maior número deles é {num2}')
            print('=' * 20)
            load = int(input('Agora, digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
    elif load == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        load = int(input('Agora, digite qual operação deseja fazer: \n[1] SOMA\n[2] MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR\n: '))
        print('=' * 20)