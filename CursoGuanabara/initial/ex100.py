from random import randint
lista = []
def sorteio(lista):
    for num in range(0,5):
        lista.append(randint(1,10))
    return lista
def soma(lista):
    scope = 0
    for num in lista:
        if num % 2 == 0:
            scope += num
    return scope
print(f'Os valores sorteados foram {sorteio(lista)}. \nA soma dos pares é {soma(lista)}')    