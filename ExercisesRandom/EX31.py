todos = []
par = []
impar = []
for x in range (0, 20):
    user = int(input('Digite um número: '))
    if user % 2 == 0:
        par.append(user)
    else:
        impar.append(user)
    todos.append(user)
print(f'Todos os números são {todos}. \nO total de pares é de {len(par)} e eles são {par} \nO total de ímpares é {len(impar)} e {impar}.')