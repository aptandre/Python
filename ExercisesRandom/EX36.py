first = []
second = []
third = []
for x in range(0, 10):
    a = input('Digite um número: ')
    first.append(a)
for y in range(0, 10):
    b = input('Digite a segunda leva de números: ')
    second.append(b)
for z in range(0,10):
    third.append(first[z])
    third.append(second[z])
print(third)