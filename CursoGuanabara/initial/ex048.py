soma = 0
for x in range (1, 501, 2):
    if x % 3 == 0:
        soma += x
print(f'O número 3 possui a soma {soma} de seus múltiplos ímpares entre 1 e 500')