Hasagi = 0
Python = 0
Elder = 0
print('-' * 25)
print('Bem vindo às eleições 2020!')
eleitores = int(input('Digite quantos eleitores haverão: '))
for x in range(1, eleitores + 1):
    voto = input('Digite em quem você irá votar: ').strip().title()
    if voto in "Hasagi":
        Hasagi += 1
    if voto in "Python":
        Python += 1
    if voto in 'Elder':
        Elder += 1
print(f'O total de votos para o candidato Python foi {Python}\nPara Hasagi foi {Hasagi}\nPara Elder foi {Elder}')