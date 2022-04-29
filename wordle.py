from tkinter import *
from tkinter.ttk import *
from random import randint

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordle")
        self.configure(background="#121213")
        self.makewidgets()
        
            
    def makewidgets(self):
        padding = {'padx' : 2, 'pady' : 2}
        textWidth = 2
        textHeight = 2
        a_1 = Label(text="A", width=2, height=2).grid(row=0, column=0, **padding)
        a_2 = Label(text="A", width=2, height=2).grid(row=0, column=1, **padding)
        a_3 = Label(text="A", width=2, height=2).grid(row=0, column=2, **padding)
        a_4 = Label(text="A", width=2, height=2).grid(row=0, column=3, **padding)
        a_5 = Label(text="A", width=2, height=2).grid(row=0, column=4, **padding)
        b_1 = Label(text="A", width=2, height=2).grid(row=1, column=0, **padding)
        b_2 = Label(text="A", width=2, height=2).grid(row=1, column=1, **padding)
        b_3 = Label(text="A", width=2, height=2).grid(row=1, column=2, **padding)
        b_4 = Label(text="A", width=2, height=2).grid(row=1, column=3, **padding)
        b_5 = Label(text="A", width=2, height=2).grid(row=1, column=4, **padding)

    def wordle(self, guess):
        with open('sgb-words.txt', 'r') as words:
            wordlist = words.read().splitlines()
            active_word = wordlist[randint(0, 1500)]




if (__name__ == "__main__"):
    app = App()
    app.mainloop()