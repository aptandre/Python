'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. Depois altere-o para que só aceite valores entre 0 e 1000'''
conjunto = int(input('Digite quantos números estarão no conjunto: '))
menor = 0
maior = 0
switch = True
for x in range(0, conjunto):
    z = int(input("Digite um número: "))
    '''while z < 0 or z > 1000:
        print('ERRO!')
        z = int(input('Digite um número: '))'''
    if switch == True:
        menor = z
        switch = False
    if z > maior:
        maior = z
    if z < menor:
        menor = z
print(f'Existem {conjunto} elementos nesse conjunto. O maior número é {maior} e o menor número é {menor}')