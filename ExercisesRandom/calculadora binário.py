num = int(input('Digite um número: '))
binary = []
while num >= 1:
    binary.append(num % 8)
    num = num // 8
for num in binary[::-1]:
    print(num, end='')
