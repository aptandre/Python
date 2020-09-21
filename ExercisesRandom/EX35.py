doragon = []
soma = 0
for x in range(0, 10):
    a = int(input('Digite um número: '))
    doragon.append(a)
    print('-'*25)
for x in doragon:
    soma += x ** 2
print(f'A soma dos quadrados dos números é: {soma}')