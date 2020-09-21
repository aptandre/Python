def voto(ano):
    import datetime
    age = datetime.datetime.now().year - ano
    if age < 16:
        return print(f'Com {age} anos você não vota.')
    elif age >= 16 and age < 18 or age > 65:
        return print(f'Com {age} anos o seu voto é opcional.')
    elif age >= 18 and age <= 65:
        return print(f'Com {age} anos o seu voto é obrigatório.')

user = int(input('Digite em que ano você nasceu: '))
voto(user)