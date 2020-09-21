frase = input('Digite uma frase: ')
viado = frase.split()
p = ''.join(viado)
q = ''.join(viado)
if p == q[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')

#Com o for for letra in range(len(junto) -1, -1, -1):