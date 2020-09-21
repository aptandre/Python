import datetime
a = datetime.date.today().year
nascimento = int(input('Digite a data do seu nascimento: '))
classificação = a - nascimento
if classificação <= 9:
    print('Você irá participar na categoria \033[0;34mmirim \033[m')
elif classificação > 9 and classificação <=14:
    print('Você irá participar na categoria \033[0;30minfantil\033[m')
elif classificação > 14 and classificação < 19:
    print('Você irá participar na categoria \033[0;32mjunior\033[m')
elif classificação >= 19 and classificação <= 20:
    print("Você irá participar na categoria \033[0;33mSênior\033[m")
elif classificação > 20:
    print('Você irá participar na categoria \033[0;31mMaster\033[m')