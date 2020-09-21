x = 0
total = 0
p = input('Pressione S e aperte enter para começar. ').strip().title()
while p not in "fFacaboufimFimAcabou":
    Produto = float(input('Digite o valor do produto: '))
    if Produto == 0:
        break
    total += Produto 
    x += 1
valor = float(input('Digite o valor recebido em dinheiro: '))
print(f'O total de produtos foi igual a {x}, o dinheiro recebido foi R${valor} e o troco será de R${valor - total}.')