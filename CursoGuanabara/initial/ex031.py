viagem = float(input('Digite a quantidade de km da viagem: '))
if viagem <= 200:
    print(f'Você irá gastar {viagem / 2} reais com essa viagem')
elif viagem <= 0:
    print('Fique onde está!')
else:
    print(f'Você irá gastar {viagem * 0.45} reais com essa viagem')