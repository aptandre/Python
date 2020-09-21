salary = float(input('Qual é o seu salário?' ))
Inss = salary * 0.08
Sindicate = salary * 0.05
IR = salary * 0.11
salaryl = salary - Inss - Sindicate - IR
print(f'O seu salário bruto é de: {salary} \n -{Inss} do INSS \n -{Sindicate} para o sindicato \n -{IR} do imposto de renda \n O seu salário líquido é de {salaryl}')
