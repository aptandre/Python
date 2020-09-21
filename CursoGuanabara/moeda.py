from monetary import monetary

def aumentar(preço, v, form=False):
    valor = float(preço) + v
    if form == False:
        return valor
    else:
        return monetary(valor)

#Uma dica: return valor if form is False else return monetary(valor)

def diminuir(preço, v, form=False):
    valor = float(preço) - v
    if form == False:
        return valor
    else:
        return monetary(valor)

def metade(preço, form=False):
    valor = float(preço) / 2
    if form == False:    
        return valor
    else:
        return monetary(valor)

def dobro(preço, form=False):
    valor = float(preço) * 2
    if form == False:
        return valor
    else:
        return monetary(valor)

def resumo(valor, Amais, Amenos):
    return print(f'\nO aumento do valor é {aumentar(valor, Amais, True)} \nO desconto do valor é {diminuir(valor, Amenos, True)} \nO dobro do valor é {metade(valor, True)} \nA metade do valor {dobro(valor, True)}')