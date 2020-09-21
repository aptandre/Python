vel = float(input('Digite a velocidade do carro(em km/h): '))
if vel > 80:
    excedente = vel - 80
    multa = excedente * 7
    print(f'O carro está muito rápido! \n Uma multa de {multa} reais será aplicada pois o carro excedeu {excedente} km/h permitidos.')
elif vel < 0:
    print('Velocidade inválida.')
elif vel == 0:
    print('O carro está parado.')
else:
    print(f'O carro está andando a {vel} km/h e está dentro do limite permitido')