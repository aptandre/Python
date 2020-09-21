'''salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salary = float(input('Digite aqui o seu salário: '))
salaryb =  salary
if salary <= 280.0:
    salary = salary + (salary * 0.2)
    x = '20'
    y = 0.2
elif salary > 280 and salary <= 700:
    salary = salary + (salary * 0.15)
    x= '15'
    y= 0.15
elif salary > 700 and salary < 1500.0:
    salary = salary + (salary * 0.1)
    x = '10'
    y = 0.1
elif salary < 0:
    print('Valor inválido.')
else:
    salary = salary + (salary * 0.05)
    x = '5'
    y = 0.05
print(f'O seu salário antes era de {salaryb} \n O percentual de aumento aplicado foi de {x}% \n O valor do aumento foi de {salaryb * y} \n O seu salário agora é {salary}')
