a1 = int(input('Digite o primeiro termo da pA: '))
n = int(input('Digite o enésimo termo da pA: '))
r = int(input('Digite a razão dessa pA: '))
n = a1 + (n-1)*r
for x in range(a1, n+1, r):
    print(x, end=' > ')