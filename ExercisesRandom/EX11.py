tipo = input('Qual o tipo de carne que você deseja? ').strip().title()
quantidade = float(input(f'Quanto de {tipo} você quer? '))
if tipo == 'Filé Duplo' or tipo == 'File Duplo':
    if quantidade <=5:
        preço = quantidade * 4.9
        preço = preço - (preço * 0.05)
        print(f'Para {quantidade} kg de Filé Duplo você deverá pagar {preço:.2f}')
    elif quantidade > 5:
        preço = quantidade * 5.8
        preço = preço - (preço * 0.05)
        print(f'Para {quantidade} kg de Filé Duplo você deverá pagar {preço:.2f}')
elif tipo == 'Alcatra':
    if quantidade <= 5:
        preço = quantidade * 5.9
        preço = preço - (preço * 0.05)
        print(f'Para {quantidade} kg de Alcatra você deverá pagar {preço:.2f}')
    elif quantidade > 5:
        preço = quantidade * 6.8
        preço = preço - (preço * 0.05)
        print(f'Para {quantidade} kg de Alcatra você deverá pagar {preço:.2f}')
elif tipo == 'Picanha':
    if quantidade <=5:
        preço = quantidade * 6.9
        preço = preço - (preço * 0.05)
        print(f'Para {quantidade} kg de Picanha você deverá pagar {preço:.2f}')
    elif quantidade > 5:
        preço = quantidade * 7.8
        preço = preço - (preço * 0.5)
        print(f'Para {quantidade} kg de Picanha você deverá pagar {preço:.2f}')