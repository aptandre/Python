import random
a = random.randint(1,10)
contador = 0
user = int(input('Digite um número: '))
while user != a:
    print(f'Você não conseguiu adivinhar! Eu estava pensando no número {a}')
    contador += 1
    a = random.randint(1,10)
    user = int(input('Digite um número: '))
print(f'Você conseguiu adivinhar! E só levou {contador} tentativas!')