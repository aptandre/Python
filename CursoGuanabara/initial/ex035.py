a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor da reta b: '))
c = float(input('Digite o valor da reta c: '))
sweep = False
sweepa = False
sweepb = False
if a + b > c:
    sweep = True
if b + c > a:
    sweepa = True
if c + a > b:
    sweepb = True
if sweep ==  True and sweepa == True and sweepb == True:
    print('Dá para formar um triângulo com essas três retas!')
    switchT = True
else:
    print('Não dá para formar um triângulo com essas três retas.')

if switchT == True:
    if a != b != c != a:
        print('Formará um triângulo escaleno.')
    if a == b == c:
        print('Formará um triângulo equilátero')
        switchT == False
    if a == b and a != c or a == c and a != b or b == c and b != a:
        print('Formará um triângulo isósceles')

#Anotações do curso:  if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
#print (f'As retas {n1}, {n2} e {n3} formam um triângulo.')
#um extra: dá para organizar os números de uma lista com o comando sorted(lista)
#Implementei a parte que diz qual tipo de triângulo é ;)