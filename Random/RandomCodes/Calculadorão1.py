print("Olá, bem vindo à calculadora summoner's Rift!")
print("Digite 1 para equação do segundo grau.")
print("Digite 2 para progressão aritmética.")
print("Digite 3 para Juros Simples.")
print("Digite 4 para Somatório.")
Cálculo = int(input("Qual tipo de cálculo nós faremos hoje? "))

dontrunAgain = True
if Cálculo <= 0 or Cálculo > 4:
    dontrunAgain = False
while dontrunAgain == True:
    if Cálculo == 1:
            a = int(input("Coloque o valor de a: "))
            b = int(input("Coloque o valor de b: "))
            c = int(input("Coloque o valor de c: "))
            delta = (b **2) - (4 * a * c)
            rDelta = delta **(1/2)
            if delta > 0:
                x1 = (-b + rDelta) // (2 * a)
                x2 = (-b - rDelta) // (2 * a)
                print("O x1 é ", x1)
                print("O x2 é ", x2)
            elif delta == 0:
                x1: -(b) / (2*a)
                print("As raízes serão iguais a: ", x1)
            elif delta < 0:
                print("Esta equação não possui raízes reais.")

    elif Cálculo == 2:
        n = int(input("Coloque o valor da posição ocupada pelo número: "))
        r = int(input("Coloque o valor da razão: "))
        a1 = int(input("Coloque o valor do primeiro termo: "))
        pA = a1 + ((n-1)*r)
        print("O termo n da P.A é igual a ", pA)

    elif Cálculo == 3:
        C = int(input("Coloque o valor do capital investido: "))
        i = float(input("Coloque o valor da taxa: "))
        t = int(input("Coloque o tempo em meses: "))
        J = C*i*t
        print("O valor dos juros será igual a: ", J)
        
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

while dontrunAgain == False:
        print("NÃO TEM ESSA OPÇÃO SEU PORRA.")
        Cálculo = int(input("Qual tipo de cálculo nós faremos hoje? "))
