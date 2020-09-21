aluno = {'nome': input('Aluno: '), 'média': float(input('Média: '))}
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print('\n')
for k, v in aluno.items():
    print(f'{k} = {v}')