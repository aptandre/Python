wis = []
while True:
    plate = input('Deseja adicionar um número? [S/N] ').strip().capitalize()
    if plate in 'Sim':
        lola = int(input('Digite um número: '))
        while lola in wis:
            lola = int(input('Número já adicionado! Digite um número: '))
        else:
            wis.append(lola)
    else:
        break
pleau = sorted(wis)
print(f'Os números adicionados à lista foram: {pleau}')


