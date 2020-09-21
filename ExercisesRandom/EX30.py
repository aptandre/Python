user = input('Digite até 10 caracteres: ')
while len(user) < 0 or len(user) > 10:
    user = input('Digite até o LIMITE  de 10 caracteres: ')
all = len(user)
#a, e, i, o, u = 0, 0, 0, 0, 0
a = user.count('a')
e = user.count('e')
i = user.count('i')
o = user.count('o')
u = user.count('u')
s = user.count(' ')
x = a + e + i + o + u + s
print(f'O número de consoantes é {all - x}')
