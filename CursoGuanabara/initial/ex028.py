import random
x = [1,2,3,4]
random.shuffle(x)
y = x[0]
print('Estou pensando em um número de 1 a 4... Consegue adivinhar qual é?')
ad = int(input('Digite o número que você acha que eu estou pensando: '))
#pls future andre, if u still into programming don't laugh at this lmao
if ad == y:
    print('Você acertou! Parabéns!')
else:
    print(f'Você errou! Eu pensei no número {y} e não no {ad}')

#Anotações do curso, dá pra fazer com o randint
#Anotações do futuro, dá pra fazer com random.choice também