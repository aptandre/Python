from tkinter import *

class Calculator:

    '''Basicamente, tem essa função principal aqui, que significa que cada vez que você criar um app e der o assignment
    app = Calculator(window), você especifica que é um aplicativo que vai rodar as funções que você definir, todas
    as funções devem ser adicionadas aqui para que funcionem'''
    def __init__(self, window):
        self.window = window

        self.create_background()

        self.create_buttons()

    def create_background(self):
        self.window.title('Cockulator')
        self.window.geometry('210x280')
        self.window.resizable(height=False, width=False)

    def create_buttons(self):
        one = Button(self.window, text='1', width=5, height=3, font=('Pokemon R/S', 9))
        one.place(x=0, y=99)

        two = Button(self.window, text='2', width=5, height=3, font=('Pokemon R/S', 9))
        two.place(x=40, y=99)

        three = Button(self.window, text='3', width=5, height=3, font=('Pokemon R/S', 9))
        three.place(x=80, y=99)

        four = Button(self.window, text='4', width=5, height=3, font=('Pokemon R/S', 9))
        four.place(x=0, y=159)

        five = Button(self.window, text='5', width=5, height=3, font=('Pokemon R/S', 9))
        five.place(x=40, y=159)

        six = Button(self.window, text='6', width=5, height=3, font=('Pokemon R/S', 9))
        six.place(x=80, y=159)

        seven = Button(self.window, text='7', width=5, height=3, font=('Pokemon R/S', 9))
        seven.place(x=0, y=220)

        eight = Button(self.window, text='8', width=5, height=3, font=('Pokemon R/S', 9))
        eight.place(x=40, y=220)

        nine = Button(self.window, text='9', width=5, height=3, font=('Pokemon R/S', 9))
        nine.place(x=80, y=220)



window = Tk()
app = Calculator(window)
window.mainloop()