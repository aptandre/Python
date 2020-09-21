lista = []
import numpy
for x in range(0,5):
    num = int(input('Digite o número: '))
    lista.append(num)
print(f'A soma dos números é: {sum(lista)}\nA multiplicação dos números é: {numpy.prod(lista)}') 