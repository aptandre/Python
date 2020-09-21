print('=' * 20)
print("Vamos jogar jokenpo!")
repeater = True
import random
moves = ['Pedra', 'Papel', 'Tesoura']
while repeater == True:
    you = input('Qual vai ser a sua jogada? ').strip().title()
    random.shuffle(moves)
    computer = moves[0]
    if you == computer:
        print('\033[0;33mEmpate! \033[m')
        print('-' * 20)
    elif you == 'Tesoura':
        if computer == 'Papel':
            print(f'O computador escolheu {computer} e você \033[0;32mganhou! \033[m')
            print('-' * 20)
        elif computer == 'Pedra':
            print(f'O computador escolher {computer} e você \033[0;31mperdeu! \033[m')
            print('-' * 20)
    elif you == 'Papel':
        if computer == 'Pedra':
            print(f'O computador escolheu {computer} \033[0;32mganhou! \033[m')
            print('-' * 20)
        if computer == 'Tesoura':
            print(f'O computador escolheu {computer} \033[0;31mperdeu! \033[m')
            print('-' * 20)
    elif you == 'Pedra':
        if computer =='Tesoura':
            print(f'O computador escolheu {computer} \033[0;32mganhou! \033[m')
            print('-' * 20)
        if computer == 'Papel':
            print(f'O computador escolher {computer} \033[0;31mperdeu! \033[m')
            print('-' * 20)
    elif you == 'Stop':
        repeater = False
print('Bye!')