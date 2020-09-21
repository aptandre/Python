from time import sleep
def escreve(string):
    linha = len(string)
    print('\033[0;30;42m')
    print('~' * linha)
    print(string)
    print('~' * linha)

def pyHelp (comando):
    escreve('Recolhendo informações...')
    print('\033[0;30;107m')
    sleep(0.3)
    return help(comando)

escreve('Sistema de ajuda pyHelp!')
print('\033[0;30;m')
pabbles = input('Digite uma biblioteca ou comando que deseja saber: ')
pyHelp(pabbles)