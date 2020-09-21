aprovados = []
x = 0
acum = 0
media = []
for x in range(1, 11):
    nota1 = int(input(f'Digite as notas do aluno {x}: '))
    nota2 = int(input(f'Digite as notas do aluno {x}: '))
    nota3 = int(input(f'Digite as notas do aluno {x}: '))
    nota4 = int(input(f'Digite as notas do aluno {x}: '))
    print('='*25)
    acum = (nota1 + nota2 + nota3 + nota4) / 4
    media.append(acum)
    x += 1
    if acum >= 7:
        aprovados.append(acum)
print(f'Estas são todas as médias: {media}\nE esta é a quantidade de alunos aprovados: {len(aprovados)}')