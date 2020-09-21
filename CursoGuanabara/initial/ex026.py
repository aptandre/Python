frase = input('Digite uma frase aqui: ').capitalize().strip().lower()
var = input('Digite uma letra a ser buscada: ').capitalize().strip().lower()
print(f'A letra {var} apareceu pela primeira vez na posição {frase.find(var) + 1}')
print(f'A letra {var} apareceu pela última vez na posição {frase.rfind(var) + 1}')
print(f'A letra {var} apareceu {frase.count(var)} vezes na frase')
#Dei uma travada nessa porque não sabia do rfind para começar a direita e não da esquerda