'''desenvolva um programa que leia nome, idade e sexo de 4 pessoas e mostre: 
a media de idades - 
nome do homem mais velho
quantas mulheres tem menos de 21 anos
update: Fiz com for e class, ou seja, POO, o Guanabara fez de uma forma diferente, sucinta e beeem mais prática, eu reconheço,
mas este código aqui teve algumas sacadas sobre mim as quais eu não esperava, por isso, eu o deixarei intacto
Uma anotação interessante do curso: Para escolhas como "masculino", "homem", "m" "H" dá para colocar tudo isso em um string só 'masculinomhomemh' e, se tiver em algum desses parametros vai reconhecer com um "in" '''
class Human:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender
lista =[]
ages = []
minor = []
homi = []
i = 0
b = 0
def Soma(element, elemento, elementoo, elementooo):
    sumb = (element + elemento + elementoo + elementooo) / 4
    return print(f'A média das idades é {sumb}')
for x in range(0, 4):
    nome = input('Digite o seu nome: ').strip().title()
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu gênero: ').strip().title()
    print('=' * 20)
    ackn = nome
    ackn = Human(nome, idade, sexo)
    lista.append(ackn)
for x in lista:
    print(f'Nome: {lista[i].name}')
    print(f'Idade: {lista[i].age}')
    ages.append(lista[i].age)
    print(f'Sexo: {lista[i].gender}')
    print('-' * 20)
    if lista[i].age >= 21 and lista[i].gender == 'Feminino':
        minor.append(lista[i])
    if lista[i].gender == 'Masculino':
        homi.append(lista[i].age)
    i += 1
Soma(ages[0], ages[1], ages[2], ages[3])
if len(minor) > 0:
    print(f'Tem {len(minor)} mulheres com 21 anos ou mais')
w = max(homi)
for a in lista:
    if lista[b].age == w:
        print(f'O homem com a maior idade é o {lista[b].name} com {lista[b].age} anos!')
    b += 1