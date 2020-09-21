contador = 1
num = int(input('Digite um número: '))
total = maior = menor = num
resp = input('Deseja digitar um valor? [S/N]: ').strip().upper()
while resp == 'S':
    contador += 1
    num = int(input('Digite um número: '))
    total += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = input('Deseja digitar um valor? [S/N]: ').strip().upper()
print(f'O maior número é {maior}\no menor número é {menor}\na quantidade de valores foi {contador}\na média entre os valores é {total/contador}')