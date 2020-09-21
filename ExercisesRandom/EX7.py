datad = int(input('Digite um dia: '))
datam = int(input('Digite um mês: '))
datay = int(input('Digite um ano: '))
if datay%4==0 and datay%100!=0 or datay%400==0:
    leap = True
else:
    leap = False
thirtyone = [10, 12, 1, 3, 5, 7, 8]
thirty = [4, 6, 7, 11]
if datam in thirtyone:
    if datad < 0 or datad > 31:
        print('Data inválida')
    else:
        print(f'A data {datad}/{datam}/{datay} é uma data válida.')
elif datam in thirty:
    if datad < 0 or datad > 30:
        print('Data inválida')
    else:
        print(f'A data {datad}/{datam}/{datay} é uma data válida')
elif datam == 2:
    if leap == True:
        if datad < 0 or datad > 29:
            print('Data inválida')
        else:
            if datad < 0 or datad > 28:
                print(f'A data {datad}/{datam}/{datay} é uma data válida')