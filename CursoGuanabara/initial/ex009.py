'''num = float(input('Digite um número para ver sua tabuada: '))
n = 1
print('-------------------')
while n <= 10:
    print(f'{num:.0f} x {n} = {num * n:.0f}')
    n = n + 1
print('-------------------')'''

'''Notas de revisão de código (30/07/2020):
O código tem a aproximação decimal na exibição, só que precisa ter no cálculo também
Se eu colocar 12.5, é exibido o 12 e calculado o 12.5'''

user = input('Digite um número para ver a sua tabuada: ')
user = int(user)
n = 1
print('-'*20)
while n <= 10:
    print(f'{user} x {n} = {user * n}')
    n += 1
print('-'*20)
