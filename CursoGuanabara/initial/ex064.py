numero = contador = soma = 0
numero = int(input('Digite um número: '))
while numero != 999:
    soma += numero
    numero = int(input('Digite um número: '))
    contador += 1
print(f'No total, foram {contador} números e a soma deles foi igual a {soma}.')
'''Lembrar de colocar a variável antes do while para que ela seja reconhecida e caia fora do while com o contador -1'''