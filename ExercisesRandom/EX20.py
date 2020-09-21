'''EXERCÍCIO TRI'''
listaf = []
listam = []
listad = []
x = 0
for x in range(0, 10):
    if x == 0:
        resposta1 = input('Digite a resposta da primeira questão: ').strip().capitalize()
        if resposta1 == 'A':
            listaf.append(x)
    if x == 1:
        resposta2 = input('Digite a resposta da segunda questão: ').strip().capitalize()
        if resposta2 == 'E':
            listad.append('E')
    if x == 2:
        resposta3 = input('Digite a resposta da terceira questão: ').strip().capitalize()
        if resposta3 == 'C':
            listad.append('C')
    if x == 3:
        resposta4 = input('Digite a resposta da quarta questão: ').strip().capitalize()
        if resposta4 == 'E':
            listaf.append('E')
        else:
            if len(listad) > 0:
                del listad[0]
    if x == 4:
        resposta5 = input('Digite a resposta da quinta questão: ').strip().capitalize()
        if resposta5 == 'C':
            listam.append('E')
    if x == 5:
        resposta6 = input('Digite a resposta da sexta questão: ').strip().capitalize()
        if resposta6 == 'D':
            listaf.append('E')
        else:
            if len(listad) > 0:
                del listad[0]
    if x == 6:
        resposta7 = input('Digite a resposta da sétima questão: ').strip().capitalize()
        if resposta7 == 'A':
            listam.append('E')
    if x == 7:
        resposta8 = input('Digite a resposta da oitava questão: ').strip().capitalize()
        if resposta8 == 'B':
            listam.append('E')
    if x == 8:
        resposta9 = input('Digite a resposta da nona questão: ').strip().capitalize()
        if resposta9 == 'B':
            listam.append('E')
    if x == 9:
        resposta10 = input('Digite a resposta da décima questão: ').strip().capitalize()
        if resposta10 == 'E':
            listaf.append('E')
        else:
            if len(listad) > 0:
                del listad[0]
print(f'A sua nota foi {len(listaf) + len(listad) + len(listam)}')