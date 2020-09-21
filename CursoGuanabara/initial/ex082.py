alista = []
blista = []
clista = []
while True:
    a = input('Digite um número: ')
    if a == 'pare':
        break
    alista.append(int(a))
for x in alista:
    if x % 2 == 0:
        blista.append(x)
    else:
        clista.append(x)
print(f'A lista: {alista} \nA lista de pares: {blista} \nA lista de ímpares: {clista}')