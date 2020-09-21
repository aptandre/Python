import moeda
from utilidadescev.dados import dinheiro

#valor = input('Digite um valor: ')
#valor = dinheiro.leiaDinheiro(valor)
valor = dinheiro.leiaDinheiro('Coloque: ')
Amenos = int(input('Digite o desconto: '))
Amais = int(input('Digite o valor que vai ser adicionado: '))
moeda.resumo(valor, Amais, Amenos)