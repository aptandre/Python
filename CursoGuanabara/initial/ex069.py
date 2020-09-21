homi = muie = dezoito = muie21 = 0
p = 'S'
while p in 'sSsimSim':
    nome = input('Digite o seu nome: ')
    sexo = input('Digite o seu sexo: ')
    while sexo not in 'hHomemhomemhomimMulherfemininofFmuie':
        sexo = input('Erro! Digite o seu sexo: ')
    idade = int(input('Digite a sua idade: '))
    if sexo in 'hHomemhomemhomi':
        homi += 1
    elif sexo in 'mMulherfemininofFmuie':
        muie += 1
        if idade > 21:
            muie21 += 1
    if idade > 18:
        dezoito+= 1
    p = input('Deseja cadastrar outra pessoa? ')
    print('-' *20)
print(f'No final foram recebidas {homi + muie} entradas.\n{homi} São homens.\n{muie} São mulheres.\n{dezoito} deles tem mais de 18 anos.\n{muie21} mulheres têm mais de 21 anos')
