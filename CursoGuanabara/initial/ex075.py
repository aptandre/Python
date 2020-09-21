p = nove = par = pep = three = 0
tupla = ()
#ps: para evitar de utilizar um WHILE para fazer uma tupla com inputs do usuário, dá para colocar tupla = input(), input(), input(), input()
while p < 4:
    a = input('Digite um número: ')
    #a = str(a)
    a = tuple(a)
    tupla = tupla + tuple(a)
    p += 1
for x in tupla:
    x = int(x)
    if x % 2 == 0:
        par += 1
    if x == 9:
        nove += 1
    pep += 1
    if x == 3:
        three += 1
        if three >= 1:
            print(f'O número três apareceu na posição {pep}')
if three == 0:
    print('O número três não apareceu em nenhuma posição.')
print(f'A quantidade de números pares é {par}\nA quantidade de números 9 é {nove}')
#Para o nome tupla.count(9), para o 3 tupla.index(3)