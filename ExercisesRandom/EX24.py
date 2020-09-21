num = int(input('Digite o número e eu direi a sua tabuada: '))
x = int(input('A tabuada começará por: '))
y = int(input('E terminará em: '))
while y < x:
    print('Inválido!')
    y = int(input('A tabuada terminará em: '))
while x <= y:
    print(f'{num} x {x} = {num * x}')
    x += 1