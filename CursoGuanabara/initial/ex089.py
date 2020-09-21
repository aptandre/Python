boletim = []
while True:
    nome = input('\nDigite o nome: ')
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, nota1, nota2, media])
    continuar = input('\nDeseja continuar? [S/N]')
    if continuar in 'nNNaonaonope':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Qual o índice do aluno? (999 interrompe) '))
    if opc == 999:
        print('Processo finalizado')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]} e {boletim[opc][1]}')





#The code down bellow is the one I was trying to do when I actually gave up and went for the resolution.

'''boletim = []
posi = 0
while True:
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    boletim.append(aluno)
    boletim.append(nota1)
    boletim.append(nota2)
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'nNnaoNao':
        break
for aluno in boletim[::3]:
    pos = boletim.index(aluno)
    media = (boletim[pos+1] + boletim[pos+2]) / 2
    print(f'Aluno Nº {posi} = {boletim[pos]} | Média: {media:.1f}')
    posi += 1
while True:
    dado = int(input("Deseja acessar as notas de qual aluno?(999 para) "))
    if dado == 999:
        print('Processo finalizado')
        break
    elif dado == 0:
        print(f'Notas {boletim[1]} | {boletim[2]} \n')
    else:
        x = dado * 3 - 5
        print(f'Notas {boletim[x]} | {boletim[x+1]} \n')
        x = 0'''