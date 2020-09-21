import math as m
valorcasa = float(input('Digite o valor da casa: '))
valorsalario = float(input('Digite o valor do seu salário: '))
anos = float(input('Digite em quantos anos deseja pagar: '))
prest = m.ceil(valorcasa / (anos * 12))
if prest > (valorsalario*0.3):
    print('O empréstimo foi negado.')
else:
    print('O empréstimo foi aprovado.')