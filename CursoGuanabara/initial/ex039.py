import datetime
ano = int(input('Digite o ano em que você nasceu: '))
a = datetime.date.today().year
if a - ano == 18:
    print('Você precisa se alistar nesse ano.')
elif a - ano < 18:
    excedente = 18 - (a - ano)
    print(f"Você precisará se alistar em {excedente} anos!")
elif a - ano > 18:
    excedente = (a-ano) - 18
    print(f'Já deveria ter se alistado há {excedente} anos')