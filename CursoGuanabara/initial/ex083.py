frase = input('Digite uma expressão: ')
aberto = []
fechado = []
if frase.count('(') == frase.count(')'):
    print('É válido!')
else:
    print('Inválido!')
'''for p in frase:
    if p == '(':
        aberto.append(p)
    elif p == ')':
        fechado.append(p)
if len(aberto) == len(fechado):
    print('Válido!')
else:
    print('Inválido')'''
#The 2 above were made by me
#Update pós correção: Não dá para fazer com len(lista) porque, no fim, não vai detectar erros em expressões que estão, por exemplo, em )a+b(. Optar, pois, pela solução abaixo.



#This one down below I got it from the internet
''''open_list = ['{', '[', '(']
closed_list = ['}', ']', ')']
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            per = close_list.index(i)
            if len(stack) > 0 and open_list(per) == stack[len(stack)-1]:
                stack.pop()
            else:
                return 'Unbalanced'
    if len(stack) == 0:
        return 'Balanced'''