anoinicial = 1995
salary = 1000
x = 0.015
while anoinicial < 2020:
    anoinicial += 1
    salary += (salary*x)
    x *= 2
    print(f'Ano: {anoinicial} Salário: {salary:.2f}')
