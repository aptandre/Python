#Esse eu dei uma copiada porque nem na aula do fábio eu entendi
num = int(input('Digite o número de até 5 dígitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
#nota a se lembrar: aqui, dividir por 100 fica como se fosse dividir 10 e depois dividir por 10 (matematicamente falando também)
print(f'Unidade:{u}, Dezena:{d}, Centena:{c}, Milhar:{m}')
print(u+d+c+m)