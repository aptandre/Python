limite = int(input('Digite um limite: '))
catch_me = 0
if limite == 1:
    print(1)
a, b, c = 1, 1, 0
while catch_me < limite - 1:
    c += a
    a, b = b, c
    catch_me += 1
    print('1 1' if c == 1 else c, end=' ')