from math import sqrt as rq
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = rq(cateto_adjacente ** 2 + cateto_oposto ** 2)
print(f'A medida da hipotenusa é {hipotenusa:.2f}')

#Also, tem uma função no math que é math.hypot(x, y)