'''lista.insert(posição, valor) | lista.pop('valor opcional, caso não tenha vai deletar o último item') |
lista.remove('item específico') |  lista.sort() | lista.sort(reverse=True) a = b[:] ou a = b.copy()'''
lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'A lista {lista} possui o número {max(lista)} como maior valor e {min(lista)} como menor valor.')
print(f'O menor valor apareceu nas posições: ', end = '')
for x, v in enumerate(lista):
    if v == min(lista):
        print(f'...{x}', end='')
print()
print(f'O maior valor apareceu nas posições: ', end='')
for x, v in enumerate(lista):
    if v == max(lista):
        print(f'...{x}', end='')
        
'''notes CeV:
dentro do for:
    if c == 0:
        max == c(input)
    else:
        if userinput > max:
            max = userinput (no caso da lista seria lista[c])
        elif userinput < min:
            min = userinput'''