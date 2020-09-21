quantmo = float(input('Digite quantos quilos de morangos: '))
quantoma = float(input('Digite quantos quilos de maçã: '))
if quantmo <= 5:
    valorfmaçã = quantmo * 2.5
if quantoma <= 5:
    valorfmorango = quantoma * 1.8
elif quantmo > 5:
    valorfmaçã = quantmo * 2.2
if quantoma > 5:
    valorfmorango = quantoma * 1.5
vt = valorfmaçã + valorfmorango
if quantmo > 8 or quantoma > 8 or vt > 25.0:
    vt = vt - (vt * 0.1)
    print(f'O valor a ser pago será de R${vt}')
else:
    print(f'O valor a ser pago será de R${vt}')