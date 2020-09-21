'''tamanho em metros quadrados
1L - 3m 
1 lata - 18 L - 80 reais
1 galão - 3,6L - 25 reais'''
#THIS TOOK ME SOME TIME, BUT I WAS ABLE TO DO IT AND I'M PROUD OF IT!
import math as m
area = float(input('Digite a área a ser pintada: '))
quantidade_lata = m.ceil((area / 3) / 18)
granalata = quantidade_lata * 80
quantidade_galao = m.ceil((area / 3) / 3.6)
granagalao = m.ceil(quantidade_galao) * 25
z = quantidade_lata * 18 * 3
print(f'Para pintar essa área você precisará de {quantidade_lata} latas e gastará {granalata} reais')
print(f'Para pintar essa área você precisará de {quantidade_galao} galões e gastará {granagalao} reais ')
if z > area:
    y = z - area
    #sey = area - y
    w = m.ceil(y / 3.6)
    x = m.ceil(w / 3 / 3.6)
    lata_galao = (area / 3 / 18)
    if lata_galao < 1:
        lata_galao = m.floor(y/ 3/ 18)
        x = m.ceil((area / 3) / 3.6)
    else:
        lata_galao = m.ceil( y/ 3/ 18)
    print(f'Para pintar essa área você precisará de {lata_galao} latas e {x} galões e gastará {(lata_galao * 80) + (x * 25)} reais')
else:
    print(f'Para pintar essa área você precisará de {quantidade_lata} latas e gastará {granalata} reais')
