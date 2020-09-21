print("Olá, bem vindo à calculadora summoner's Rift!",'\n', "Digite 1 para equação do segundo grau.",'\n', 'Digite 2 para progressão aritmética.','\n',"Digite 3 para Juros Simples.",'\n',"Digite 4 para Somatório.")
Cálculo = int(input("Qual tipo de cálculo nós faremos hoje? "))
import time

def E2g (a, b, c):
    delta = (b **2) - 4 * a * c
    rDelta = delta **(1/2)
    if delta > 0:
        x1 = (-b + rDelta) // (2 * a)
        x2 = (-b - rDelta) // (2 * a)
        return x1
        return x2
    elif delta == 0:
        x1: -(b) / (2*a)
        return x1
    elif delta < 0:
        return print('Não há raízes reais para esta equação')
    
def PA (n, r, a1):
    pA = a1 + ((n-1)*r)
    return print("O termo enésimo dessa PA é", pA)

while Cálculo > 0 and Cálculo < 5:
    if Cálculo == 1:
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            c = int(input('Digite o valor de c: '))
            E2g(a, b, c)
            print('=' * 25)
            Cálculo = int(input("Deseja fazer outro cálculo? "))
    elif Cálculo == 2:
            n = int(input("Coloque o valor da posição ocupada pelo número: "))
            r = int(input("Coloque o valor da razão: "))
            a1 = int(input("Coloque o valor do primeiro termo: "))
            PA (n, r, a1)
            print('=' * 25)
            Cálculo = int(input("Deseja fazer outro cálculo? "))
    elif Cálculo == 3:
        C = int(input("Coloque o valor do capital investido: "))
        i = float(input("Coloque o valor da taxa: "))
        t = int(input("Coloque o tempo em meses: "))
        J = C*i*t
        print("O valor dos juros será igual a: ", J)
        print('=' * 25)
        Cálculo = int(input("Deseja fazer outro cálculo? "))
    elif Cálculo == 4:
        soma = 0
        valor = 1
        variante = int(input("Quantos valores iremos somar? "))
        quantv = 0
        repeater = True
        while repeater == True:
            valor = int(input("Digite um valor a ser somado: "))
            soma = soma + valor
            stop = (quantv + 1)
            quantv = (quantv +1)
            if stop == variante:
                repeater = False
                break
        print("A soma dos valores digitados é: ", soma)
        print('=' * 25)
        Cálculo = int(input("Deseja fazer outro cálculo? "))
    elif Cálculo == 5:
        print('Alright, good bye then!')
        time.sleep(0.5)
        break
if Cálculo <= 0 or Cálculo > 5:
    while Cálculo <= 0:
        print("Não existe essa opção")
        Cálculo = int(input("Qual tipo de cálculo nós faremos hoje? "))
    while Cálculo > 4:
        print("Não existe essa opção")
        Cálculo = int(input("Qual tipo de cálculo nós faremos hoje? "))
