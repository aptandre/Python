valor = int(input('Digite o valor a ser retirado: '))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if valor > 0:
        ced50 = valor // 50
        restantecinquenta = valor % 50
        if restantecinquenta >= 20:
            ced20 = restantecinquenta // 20
            restantevinte = restantecinquenta % 20
            if restantevinte < 20:
                ced10 = restantevinte // 10
                ced1 = restantevinte % 10
        elif restantecinquenta >= 10 and restantecinquenta < 20:
            ced20 = 0
            ced10 = restantecinquenta // 10
            ced1 = restantecinquenta % 10
        elif restantecinquenta < 10:
            ced1 = restantecinquenta % 10
            ced20 = ced10 = 0
        print(f'Para essa quantia, serão impressos: \n{ced50} cédulas de 50 reais \n{ced20} cédulas de 20 reais \n{ced10} cédulas de 10 reais e \n{ced1} cédulas de 1 real')
        valor = int(input('Digite outro valor a ser retirado: '))