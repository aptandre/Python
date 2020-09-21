A = int(input('Digite a população A: '))
B = int(input('Digite a população B: '))
t1 = float(input('Digite a taxa da população A, mas não em decimais: '))
t2 = float(input('Digite a taxa da população B, mas não em decimais: '))
i = 0
if A < B:
    while A < B:
        A = A + (A * (t1 / 100))
        B = B + (B * (t2 / 100))
        i = i + 1
print(f'Após {i} anos, a população de A será {A:.1f} e a população de B será {B:.1f}')