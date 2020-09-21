from random import *
from tkinter import *

root = Tk()
root.title('MadLibsGenerator!')
Texto = Text(root) #Cria a caixa de texto
Texto.pack()


def MadLibbidiup():
    global Texto
    Output = Texto.get(0.0, END) #Consegue o texto
    MadLib = Output.split() #Divide o texto em uma lista para ser um objeto fácil de manipular
    Listofwords = [] #Cria uma lista que vai separar as palavras que serão censuradas

    while True:
        word = choice(MadLib) #Escolhe uma palavra aleatória de dentro da lista
        if len(word) > 3 and word not in Listofwords: #Certifica que a palavra tem mais que 3 letras, para evitar preposições, conjunções etc. Também certifica que a palavra não já existe na lista, para que uma mesma palavra não seja adicionada duas vezes.
            Listofwords.append(word)
        else:
            while True:
                word = choice(MadLib) #Escolhe aleatoriamente de novo, certificando novamente que a palavra tem mais que 3 caracteres. Nota: ! e ? são contados, então o brilho da lua! "Lua!" passa no teste.
                if len(word) > 3:
                    break
        if len(Listofwords) == 3: #Aqui limita o máximo de palavras que você quer que suma, pode ser colocado numa variável e adaptado futuramente. Truth is: Se apertar duas vezes vai parar 6, de 6 para 9 etc. Então fica a critério da paciência do André do futuro adaptar para uma variável a escolha do usuário.
            break

    MadLib = " ".join(MadLib) #Junta a frase
    for i in Listofwords: #Substitui as palavras por frases
        if i in MadLib:
            lenI = len(i)
            MadLib = MadLib.replace(i, "_"*lenI)
        else:
            print('An error occurred.')

    Texto.delete(0.0, END)
    Texto.insert(0.0, MadLib)
    return MadLib

'''Sugestões para o futuro: Você pode também dar a opção ao usuário de ele mesmo dar as palavras que quer tirar,
fazendo com que a lisofwords seja dada por ele.'''


Btn = Button(text='Click me to madlibbidiup!', command=MadLibbidiup)
Btn.pack()




root.mainloop()