def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]

import random

def rand():
    valor = random.uniform(-1, 1)
    return valor

random.seed(1)
R = 1000
inside = []
for num in range(R):
    inside.append(rand())
    
pleito = []
for num in range(1, 10):
    pleito.append(moving_window_average(inside, num))
    
print(pleito[4][8],pleito[4][9],pleito[4][10])
print('Voce tropecara com grandes obstaculos supere e historias na vida \% %$ \'\' ¨¨')