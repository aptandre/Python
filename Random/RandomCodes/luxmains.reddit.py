def fatorial (n):
    fat = 1
    if n < 0:
        fat = 0
        print("Não existe fatorial para números negativos.")
        
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat
    
        
def Cálculo_binomial (n, k):
    return fatorial (n) / ((fatorial (n - k)) * (fatorial(k)))

def betaTester ():
    if fatorial (0) == 1:
        print("Works for 0")
    else:
        print("Doesn't work for 0")
    if fatorial (1) == 1:
        print("Works for 1")
    else:
        print("Doesn't work for 1")
    if fatorial (2) == 2:
        print("Works for 2")
    else:
        print("Doesn't work for 2")
    if fatorial (5) == 120:
        print("Works for 5")
    else:
        print("Doesn't work for 5")
    if fatorial (-1) == 0:
        print()
    else:
        print("Doesn't work for negativa numbers")
    


