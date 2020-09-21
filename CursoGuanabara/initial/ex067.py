num = int(input('Digite um número: '))
x = 1
while x <= 10:
    if num < 1:
        break
    print(f'{num} x {x} = {num*x}')
    x += 1
    if x == 11:
        x = 1
        num = int(input('Digite um número: '))
print('Domo arigatou!')
