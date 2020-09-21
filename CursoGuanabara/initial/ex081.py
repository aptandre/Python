numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = input('Deseja adicionar um valor? [S/N] ')
    if resp not in 'Ss':
        break
print(f'Você digitou {len(numeros)} itens. \nOs números em ordem decrescente são {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')