numeros = []
for x in range(0, 5):
    num = int(input('Digite os números: '))
    if x == 0 or x > numeros[-1]:
        numeros.append(num)
        print('Foi adicionado ao final da lista')
        print('-' * 30)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado à posição {pos}')
                print('-' * 30)
                break
            pos += 1
print(numeros)
#Já corrigi o código no vídeo do guanabara e ainda assim apresenta erros!


        

    