times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA','Chapecoense', 'Avaí'
w = e = place = 0
r = 20
for x in times:
    if w < 5:
        print(f'{w + 1} - {x}')
        w += 1
print('=' * 25)
#Não vi no vídeo do Guanabara mas, olhando agora era só ter associado uma variável a times[::-1] e ter printado todos os elementos (com for ou não)
for y in times[::-1]:
    if e < 5:
        print(f'{r} - {y}')
        e += 1
        r -= 1
print('=' * 25)
for z in times:
    place += 1
    if z == 'Chapecoense':
        print(f'Chapecoense está na posição {place}')
        print('-' * 25)
#times.index('Chapecoense' +1) economizaria 5 linhas! ^
times = sorted(times)
print('A lista dos times em ordem alfabética é: ')
for x in times:
    print(x, end=' | ')
'''PS: com notas do exercício, o Guanabara utilizou o fatiamento de tuplas para tornar o exercício mais sucinto e prático, mas nesse código
eu prezei também pela estética e por como as informações seriam fornecidas na tela.'''
    