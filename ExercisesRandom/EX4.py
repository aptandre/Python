arquivo = float(input('Digite o tamanho do arquivo em MB: '))
internet = float(input('Digite a velocidade da sua internet em MBPS: '))
tempo = arquivo * 8/internet / 60
print(f'O tempo que vai demorar para que o arquivo seja completamente baixado é de, aproximadamente, {tempo:.2f} minutos')