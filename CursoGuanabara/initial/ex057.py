s = input('Digite o seu sexo [M/F/NB/O]: ')
while s not in 'mfnboMFNBO':
    s = input('Erro! Digite o seu sexo [M/F/NB/O]: ')
print(f'O seu sexo é {s}')
