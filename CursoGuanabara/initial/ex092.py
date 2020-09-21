'''import datetime
datetime.datetime.now().year | USEFUL'''
cadastro = dict()
cadastro['Nome'] = input('Digite o nome: ')
cadastro['Nascimento'] = int(input('Ano de nascimento: '))
cadastro['Idade'] = 2020 - cadastro['Nascimento']
cadastro['CTPS'] = int(input('CTPS (0 = Não tem): '))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = input('Salário: ')
    aposentadoria = cadastro['Contratação']  + 35
    anoAps = aposentadoria - cadastro['Nascimento']
    cadastro['Aposentadoria'] = anoAps
print('\n' + '-'*40)
for k, v in cadastro.items():
    print(f'{k} : {v}')
    
