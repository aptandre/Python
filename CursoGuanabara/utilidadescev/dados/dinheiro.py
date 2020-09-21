'''def leiaDinheiro(valor):
    while True:
        try:
            valor = float(valor)
            break
        except ValueError:
            valor = input('VALOR INVÁLIDO! Digite um valor válido R$')
    return valor'''
#^ meu código
#Anotações do curso: reiventing the weel
#Aí lá no ex107.py você coloca a mensagem que vai ser exibida, mas não manipulada.
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Inválido!')
        else:
            válido = True
            return float(entrada)