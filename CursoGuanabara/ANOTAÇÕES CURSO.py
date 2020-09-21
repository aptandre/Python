#Anotações de códigos em código!
'''
#Conceitos a se lembrar:
Boolean
String
Float
Integer

#Módulos
math
random
fernet
time
random

#Comandos a se lembrar:
while
if
elif
else
lista.append
capitalize
import
    #from math import sqrt as square_root (Dá para importar módulos com outros nomes caso as variáveis não tenham nomes muito práticos)
    print(square_root(100))
find (texto = 'str' texto.find(s))
ord(''), para a comparação de strings e ordenação dos números
ord('a') > ord('A')
Ao definir uma função que recebe x arguments, dá para atribuir um valor "fixo" a determinado argument
CASO ele não receba outro valor pré-meditado pelo user:
def func (x, y = 5):
    return x + y
try
except: (to make exceptionsd duh)
finally: uma linha de código que vai ocorrer não importa se houver erro ou não

Anotações a se lembrar:

#MÓDULOS
No módulo time, existe uma função que permite saber o tempo desde a origem do sistema operacional usado,
utilizando time.time() dá para ver quantos segundos se passaram do primeiro dia até hoj, ademais, também dá para
usar isso para comparar o tempo que um programa demora para ser executado com variáveis de antes < e depois > com "time.time()" nas duas e subtraindo os dois valores no final.

#MANIPULAÇÃO_DE_LISTAS
Clone de lista = lista[:]
Fragmentos da lista = [x:y] (Lembrando que vai dar os elemtnos de y-x)
Adicionar elementos à lista = lista.append()
Adicionar elementos a uma posição específica da lista = lista.insert(POSIÇÃO, ELEMENTO)
Remover elementos de uma lista = lista.remove(objeto)
Contar quantas vezes um elemento aparece = lista.count(objeto)
Reverter elementos numa lista = lista.reverse() 1,2,3 = 3,2,1
for i in lista:
    print(i[0])
	esse comando devolve apenas a primeira letra do nome dos 3!
#for i in lista:
	print(i)
1
2
3
for i in range(len(lista)):
	print(i)
0, 1, 2 (Esse último comando printa a posição dos elementos da lista)

#CORES no terminal
\033[style:text:back...m

#NOTES POO:
Em POO existem classes e, dentro dessas classes, as funções definidas são chamadas de methods, os valores recebidos por
esses métodos são os arguments e, o primeiro argument em todo método de POO é "self".
Para adicionar um objeto a uma classe, você utiliza o comando objeto = classe(variável)'''

