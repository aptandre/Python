notas = 0
notaslista = []
for x in range(0, 4):
    inp = float(input('Digite as notas: '))
    notas += inp
    notaslista.append(inp)
print(f'As notas são {notaslista} e a sua média é {notas/4:.1f}')
    