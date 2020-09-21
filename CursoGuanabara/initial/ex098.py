import time
def contador(início, fim, passo):
    if início < fim:
        print(f'Contagem de {início} até {fim} de {passo} em {passo}: \n')
        for num in range(início, fim + 1, passo):
            print(num, end=' ', flush=True)
            #O flush faz com que a iteração ocorra normalmente, sem acumular o tempo para exibir tudo no final.
            time.sleep(0.3)
        print('\n' + '-'*20)
    else:
        print(f'Contagem de {início} até {fim} de {passo} em {passo}: \n')
        if passo < 0:
            passo = passo * -1
        elif passo == 0:
            passo = 1
        for num in range(início, fim - passo, (passo * -1)):
            print(num, end='  ', flush=True)
            time.sleep(0.3)
        print('\n' + '-'*20)
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)