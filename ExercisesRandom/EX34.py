tutela = []
for x in range(0, 5):
    age = int(input('Digite a idade: '))
    height = float(input('Digite a altura: '))
    print("="*20)
    tutela.append(age)
    tutela.append(height)
for x in range(0, 10, 2):
        print(f'idade: {tutela[x]} altura: {tutela[x+1]}')
        x += 1
