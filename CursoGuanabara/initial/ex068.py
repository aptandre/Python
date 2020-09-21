import random as r
cont = 0
user = int(input('Digite um valor: '))
PI = input('Você quer par ou ímpar? [P/I]: ')
pc = r.randint(0,10)
while True:
    if PI in 'pP':
        if (user + pc) % 2 == 0:
            cont += 1
            print(f'O PC escolheu {pc} e você ganhou com {cont} tentativas!')
            user = int(input('Vamos jogar novamente. Digite um valor: '))
            PI = input('Você quer par ou ímpar? [P/I]: ')
            cont = 0
        else:
            cont += 1
            print(f'O PC escolheu {pc} e você perdeu com {cont} tentativas!')
            break
    elif PI in 'iI':
        if (user + pc) % 2 == 0:
            cont += 1
            print(f'O PC escolheu {pc} e você perdeu com {cont} tentativas!')
            break
        else:
            cont += 1
            print(f'O PC escolheu {pc} e você ganhou com {cont} tentativas!')
            user = int(input('Vamos jogar novamente. Digite um valor: '))
            PI = input('Você quer par ou ímpar? [P/I]: ')
            cont = 0
'''Anotações do curso: uma outa forma poderia ser colocar o user input + o pc como TOTAL e colocar if PI in 'P' elif PI in 'I' e colocar com o total a partir dessa condicional'''