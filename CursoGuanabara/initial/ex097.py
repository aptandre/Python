def escreve(string):
    linha = len(string)
    print('~' * linha)
    print(string)
    print('~' * linha)

string = input('Digite um texto qualquer: ')
escreve(string)