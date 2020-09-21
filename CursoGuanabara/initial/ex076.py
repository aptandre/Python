p = 1
z = int(input('Digite o número de elementos: '))
tupla = ()
while p <= z:
    a = input('Digite o nome do produto: '),
    b = input('Digite o preço: '),
    tupla = tupla + a + b
    p += 1
for x in range(0, len(tupla), 2):
    print(f'Produto: {tupla[x]} | Preço: R${tupla[x+1]}')
#Adaptação(Escrita antes da resolução)