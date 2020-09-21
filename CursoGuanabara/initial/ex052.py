num = int(input('Digite um número: '))
contador = 0
for x in range(1, num+1):
    if num % x == 0:
        contador += 1
        print(f'\033[32m{x} \033[m', end='')
    else:
        print(f'\033[31m{x} \033[m', end='')
    print('\033[m', end= ' ')
if contador == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo pois ele tem {contador} divisores')
#Vai dar um errinho matemático aí porque vai dar que 1 é primo, mas não é primo! print(f'\033[31m{x} \033[m', end='') line 8