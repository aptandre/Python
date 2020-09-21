a = int(input('Número: '))
divisores = 0
for x in range (1, a+1):
    if a % x == 0:
        divisores += 1
        print(x, end=' ')
if divisores > 2:
    print('Não é primo')
else:
    print('Primo')
