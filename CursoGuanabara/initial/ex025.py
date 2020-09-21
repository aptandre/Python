#Adaptei o enunciado as well
sphinx = input('Digite a parada que deseja buscar: ').title()
rae = input('Digite o seu nome: ').title()
print(f'Há {sphinx} no nome {rae}?')
l = sphinx in rae
print(l)