gender = ['Homem', 'Mulher', 'Outro', 'Masculino', 'Feminino']
estado_civil = ['Solteiro', 'Casado', 'Viúvo', 'Divorciado', 'Solteira', 'Casada', 'Viúva', 'Divorciada']
nome = input('Digite o seu nome: ')
while len(nome) < 3:
    nome = input('Nome muito curto! Digite outro nome: ')
age = int(input('Digite a sua idade: '))
while age <= 0 or age > 150:
    age = int(input('Idade inválida. Por favor, digite a sua idade: '))
salary = float(input('Digite o seu salário: '))
while salary < 0:
    salary = float(input("Por favor, digite o valor correto do seu salário: "))
sexo = input('Por favor, digite qual o seu gênero: ').strip().capitalize()
p = sexo in gender
while p == False:
    sexo = input('Esta opção é inválida. Por favor, digite qual o seu gênero: ').strip().capitalize()
    p = sexo in gender
    if p == True:
        break
civil = input('Digite o seu estado civil: ').strip().capitalize()
q = civil in estado_civil
while q == False:
    civil = input('Estado civil inválido. Digite o seu estado civil: ')
    if q == True:
        break
print('=' *25)
print(f'Cadastro completo! O seu nome é {nome} \nA sua idade é {age} anos \nO seu salário é {salary} \nO seu gênero é {sexo}\nE o seu estado civil é {civil}')

