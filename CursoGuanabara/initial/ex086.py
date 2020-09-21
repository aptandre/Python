matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somac = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o elemento [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for l in range(0,3):
    somac += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior = c
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]", end='\t')
    print()

print(f'A soma de todos os pares é {soma} \nO maior número da segunda linha é {maior}. \nA soma de todos os números da terceira coluna é {somac}.')

'''
feito por mim vvvv com os erros de não estar tão resumido quanto poderia ser, além do uso de algumas gambiarras.
for p in matriz:
    for num in matriz[ps]:
        if num % 2 == 0:
            soma += num
    if ps == 1:
        for z in matriz[ps]:
            if z > maior:
                maior = z
    ps += 1
print(f'A soma de todos os pares é {soma} \nO maior número da segunda linha é {maior}') '''

