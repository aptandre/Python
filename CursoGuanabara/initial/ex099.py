listaParam = []
'''Esse exercício era, na verdade, para ensinar sobre múltiplos pamâmetros numa função, para
isso, era só definir a função e colocar um * no parâmetro, ex:
def Apto (* num):'''
while True:
    try:
        listaParam.append(int(input('Digite um número [String para parar]: ')))
    except ValueError:
        break
def major(lista):
    print('Os valores foram: ')
    for num in lista:
        print(num, end= ' ')
    try:
        maxim = max(listaParam)
    except ValueError:
        maxim = 'Lista vazia'
    print(f'\nO maior número da lista é: {maxim} \nAo todo, foram {len(listaParam)} parâmetros na lista.')
print(major(listaParam))
    