x = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    x += 1
    cont += num
print(f'{x} números, {cont} soma')