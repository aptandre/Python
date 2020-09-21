tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
continuar = input('Deseja começar? ').strip().title()
while continuar in 'Sim':
    user = int(input('Digite um número de 1 a 20: '))
    while user not in range(0, 21):
        user = int(input('ERRO! Por favor, digite um número de 1 a 20: '))
    print(f'Você digitou o número {tupla[user]}')
    continuar = input('Deseja continuar? ').strip().title()
    print('=' * 25)
