def fatorial(num=0, show=False):
    """Ajuda a calcula o fatorial de um número, recebe dois parâmetros, um deles sendo opcional,
caso show=True, irá mostrar a multiplicação interativa dos números."""
#Essa parte de cima é para explicar sobre a função no help(fatorial)
    if show is False:
        fatorial = 1
        for c in range(num, 0, -1):
            fatorial *= c
        return print(fatorial)
    else:
        fatorial = 1
        for c in range(num, 0, -1):
            print(f'{c} x ', end='')
            fatorial *= c
        print('=', end=' ')
        return print(fatorial)
#Para tirar o x depois do um é com if mesmo.
fatorial(5, True)
fatorial(4)
fatorial(10, True)
fatorial(13)
