larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = alt * larg
#2 m² = 1L de tinta
print(f'Você precisará de {area/2:.2f} L de tinta para pintar essa parede de área {area}')
'''Precisa especificar que é em metro! Se não o usuário coloca um rolê em cm e fode tudo.'''