def tabuada():
    from random import randint
    from datetime import datetime
    cont = erros = 0
    date = datetime.now()
    while True:
        x = randint(1, 10)
        y = randint(1, 20)
        print(f'{x} x {y} = ', end='')
        user = input()
        try:
            user = int(user)
            while user != x * y:
                user = int(input('Resposta errada, tente novamente: '))
                erros += 1
            cont += 1
        except ValueError:
            if '[' in user or ']' in user:
                user = input()
            print('Finalizado')
            with open("record.txt", "a") as record:
                record.write(f'\nForam um total de {cont} cálculos e {erros} erros. REGISTRADO EM {date}.')
            print(f'\nForam um total de {cont} cálculos e {erros} erros.')
            record
            break

tabuada()
    
def tabulada(numero):
    from random import randint, shuffle
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for n in range(20):
        shuffle(numeros)
        print(f'{numero} x {numeros[0]} = ', end='')
        res = int(input())
        while res != numero * numeros[0]:
            res = int(input('Valor errado! Digite novamente: '))
        numeros.pop(0)

def tab(n):
    from random import shuffle
    tab = [x for x in range(11)]
    for i in range(10):
        shuffle(tab)
        print(f'{n} + {tab[0]} = ', end='')
        res = int(input())
        while res != n + tab[0]:
            res = int(input('ERROU! Digite novamente: '))
        tab.pop(0)
        
