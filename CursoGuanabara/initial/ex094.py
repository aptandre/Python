people = dict()
ppllist = list()
age = cont = 0
mulheres = []
aged = []

while True:
    people['Name'] = input('Their name: ')
    people['Age'] = int(input('Age: '))
    age += people['Age']
    people['Sex'] = input('Sexo [M/F/NB]: ')
    '''uma alternativa de whiles de resposta:
    while True:
        if pessoa['sexo'] in 'MFNB':
            break
        print('ERRO!' Digite novamente.')'''
    cont += 1
    ppllist.append(people.copy())
    continuar = input('Continuar? [S/N]: ')
    print()
    if continuar in 'NnNaonopenao':
        break

print(f'O grupo tem {len(ppllist)} pessoas. \nA média de idade é de {age/cont:.1f}')

for pessoa in ppllist:
    if pessoa['Sex'] in 'fFfemeamuiemulhermogliecolher':
        mulheres.append(pessoa['Name'])
        #Ou, em vez de guardar em uma lista, print(f'{pessoa["Nome"]}', end='')
print('As mulheres cadastradas foram: ', end='')

for mulher in mulheres:
    print(mulher)

print('Pessoas acima de média de idade: ')
for pessoa in ppllist:
    if pessoa['Age'] > (age/cont):
        print(pessoa)