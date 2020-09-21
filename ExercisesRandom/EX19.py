turmas = int(input('Quantas turmas estão na escola? '))
contador = 0
x = 1
for x in range (1, turmas +1):
    alunos = int(input(f'Digite a quantidade de alunos da turma {x}: '))
    x += 1
    contador += alunos
print(f'A média de alunos por turma é de {contador/turmas:.2f}')