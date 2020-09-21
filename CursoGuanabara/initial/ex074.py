import random as r
tupla = ()
z = ()
p = 0
while p < 5:
    a = r.randint(0,10)
     a = str(a)
    a = tuple(a)
    tupla = tupla + tuple(a)
    p += 1
tupla = sorted(tupla)
print(f'A tupla {tupla} contém {tupla[0]} como menor valor e {tupla[4]} como maior valor.')
'''suggestion: Dá para randomizar a tupla com os 5 números colocando  
tupla = r.randint(0,10), r.randint(0,10), r.randint(0,10), r.randint(0,10), r.randint(0,10)
max(tupla) e min(tupla) ;D'''
    