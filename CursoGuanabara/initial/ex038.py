num1 = float(input('Digite um número inteiro: '))
num2 = float(input('Digite outro número inteiro: '))
if num1 > num2:
    print(f'O maior número é {num1}')
elif num1 < num2:
    print(f'O maior número é {num2}')
elif num1 == num2:
    print('They\'re the same')
else:
    print('Tu fez merda aí, irmão.') #<Situation handling skills 100%