peso = float(input('Qual é o peso do peixe?: '))
if peso > 50:
    excedente = peso - 50
    valor_da_multa = excedente * 4
print(f'O peixe excede em {excedente} quilos e o valor da multa será de {valor_da_multa}')
