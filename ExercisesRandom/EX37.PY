temps = []
tempsm = []
soma = 0
for x in range(0, 12):
    temp = float(input('Digite uma temperatura: '))
    month = input('Digite o mês: ')
    temps.append(month)
    temps.append(temp)
    tempsm.append(temp)
for x in tempsm:
    soma += x
soma = soma / 12
for s in range(0, 24, 2):
    if temps[s + 1] > soma:
        print(f'O mês {temps[s]} teve uma média de temperatura de {temps[s+1]}, acima da média anual de {soma} ',)
        print('=' * 20)

    