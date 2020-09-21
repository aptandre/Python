tupla = 'Sakura', 'Tomoyo', 'Syaoran', 'Yukito', 'Mei Lin', 'Fujitaka', 'Nadeshiko', 'Yue', 'Kerberus', 'Kahu', 'Eriol','Spinelson', 'Nakuro'
vowels = ''
for x in tupla:
    x = x.upper()
    if 'A' in x:
        vowels = vowels + ('a ')
    if 'E' in x:
        vowels = vowels + 'e '
    if 'I' in x:
        vowels = vowels + 'i '
    if 'O' in x:
        vowels = vowels + 'o '
    if 'U' in x:
        vowels = vowels + 'u '
    print(f'Na palvra {x} temos {vowels}')
    vowels = ''
'''Anotações da aula: 
for p in tupla:
    print(f'Na palavra {p} temos')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''