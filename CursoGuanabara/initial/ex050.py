lista = []
for x in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista.append(num)
y = 0
for x in lista:
    y += x
print(f'A soma dos números é {y}')
#Dei uma adaptada no código, não ficou igual ao da resolução mas ficou mais clean ;)
'''Código do vídeo:
soma = 0
cont = 0
for x in range(1,7):
    num = int(input('Digite o valor: ))
    if num % 2 == 0:
        soma += num
        cont += 1'''