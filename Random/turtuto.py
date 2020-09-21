import turtle
direction = int(input('Digite a direção: '))
impmon = True
while impmon == True:
    if direction == 1:
        turtle.forward(5)
        direction = int(input('Coloque esta merda novamente: '))
    if direction == 2:
        turtle.backward(5)
        direction = int(input('Coloque esta merda novamente: '))
    if direction == 3:
        turtle.right(90)
        direction = int(input('Coloque esta merda novamente: '))
    if direction == 4:
        turtle.left(90)
        direction = int(input('Coloque esta merda novamente: '))
