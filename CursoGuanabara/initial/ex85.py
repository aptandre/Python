lista_de_listas = [[], []]
for x in range(0,7):
    user = int(input(f'Digite o {x+1}º valor: '))
    if user % 2 == 0:
        lista_de_listas[0].append(user)
    else:
        lista_de_listas[1].append(user)
lista_de_listas[0].sort()
lista_de_listas[1].sort()
print(f'Os valores pares digitados foram: {lista_de_listas[0]}\nOs valores ímpares digitados foram: {lista_de_listas[1]}')