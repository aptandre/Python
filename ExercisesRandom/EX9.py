print('=' * 20)
#os whiles foram projetos que não deram certo :(
print('Responda com sim ou não para determinarmos a sua participação no crime!')
p1 = input('Você ligou para a vítima? ').strip().title()
#while p1 != 'Sim' or p1 != 'Não':
    #p1 = input('Responda corretamente, você ligou para a vítima? ').strip().title()
p2 = input('Esteve no local do crime? ').strip().title()
#while p2 != 'Sim' or p2 != 'Não':
    #p2 = input('Responda corretamente, você esteve no local do crime? ').strip().title()
p3 = input('Você mora perto da vítima? ').strip().title()
#while p3 != 'Sim' or p3 != 'Não':
    #p3 = input('Responda corretamente, você mora perto da vítima? ').strip().title()
p4 = input('Você devia dinheiro para a vítima? ').strip().title()
#while p4 != 'Sim' or p4 != 'Não':
    #p4 = input('Responda corretamente, você devia dinheiro para a vítima?').strip().title()
p5 = input('Já trabalhou com a vítima? ').strip().title()
#while p5 != 'Sim' or p5 != 'Não':
    #p5 = input('Responda corretamente, você já trabalhou com a vítima? ').strip().title()

lista = []
if p1 == 'Sim':
    lista.append(p1)
if p2 == 'Sim':
    lista.append(p2)
if p3 == 'Sim':
    lista.append(p3)
if p4 == 'Sim':
    lista.append(p4)
if p5 == 'Sim':
    lista.append(p5)

veredito = len(lista)
if veredito == 0 or veredito == 1:
    print('Você foi descartado da lista de suspeitos.')
if veredito == 2:
    print('Você é um dos suspeitos.')
if veredito == 3 or veredito == 4:
    print('Você é um dos cúmplices do crime.')
if veredito == 5:
    print('Você é o culpado.')