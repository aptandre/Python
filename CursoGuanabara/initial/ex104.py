#A parte de cima é o código que eu fiz primeiro e serviu para o exercício 113.
def leiaInt(num):
    if n == '':
        print('O usuário não digitou nenhum número.')
    else:
        while True:
            try:
                num = int(num)
                return print(f'O número {num} é válido')
            except ValueError:
                num = input('VALOR INVÁLIDO! Digite apenas números inteiros: ')
                leiaInt(num)
            break
n = input('Digite um número: ').strip()
leiaInt(n)

'''Vou copiar o código dele pois ele já utilizou
o leiaInt como input, o que é um extra da função.

def leiaInt(msg):
    ok False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!, Digite um número inteiro válido')
        if ok:
            break
    return valor'''