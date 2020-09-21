n = 0
p = 0
for x in range(0,7):
    age = int(input('Digite o ano do seu nascimento: '))
    a = 2020 - age
    if a < 18:
        n += 1
    else:
        p += 1
print(f'{n} pessoas irão atingir a maioridade e {p} já a atingiram')
