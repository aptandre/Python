lista = []
for x in range (0, 10):
    x = int(input('Digite um número: '))
    lista.append(x)
print(f'A ordem inversa dos números é: {lista[::-1]}')