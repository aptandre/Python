var = 0
f = int(input('Digite o fatorial: '))
for x in range(f - 1, 0, -1):
    f = f * x
print(f'O fatorial desse número é {f}')