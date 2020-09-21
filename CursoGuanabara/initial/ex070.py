contador = 1
miru = 0
nome = input('Digite o nome do produto: ')
minimo = nome
preço = float(input('Digite o preço do produto: '))
minimop = preço
continua = input('Deseja adicionar mais itens? ')
print('-' * 20)
while continua not in 'naonNNAOnotnopenei':
    nome = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço: '))
    contador += 1
    if preço <= minimop:
        minimop = preço
        minimo = nome
    if preço > 1000:
        miru += 1
    print('-' * 20)
    continua = input('Deseja continuar? ')
    print('-' * 20)
print(f'O total de produtos foi {contador}\nO objeto de preço mínimo foi {minimo} que custou R${minimop}')