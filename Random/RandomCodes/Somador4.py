soma = 0
valor = 1
variante = int(input("Quantos valores iremos somar? "))
quantv = 0
repeater = True
while repeater == True:
    valor = int(input("Digite um valor a ser somado: ", end = "\t"))
    soma = soma + valor
    stop = (quantv + 1)
    quantv = (quantv +1)
    if stop == variante:
        repeater = False
        break
    
print("A soma dos valores digitados é: ", soma)
