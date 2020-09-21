lista = []
for x in range (0,10):
    p = int(input('Digite um número: '))
    if p % 2 == 0:
        
        lista.append(p)
print(f'A quantidade de números pares é {len(lista)} e a quantidade de números ímpares é {10 - len(lista)}')