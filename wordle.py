from tkinter import *
from random import randint

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordle")
        self.configure(background="#121213")
        self.makewidgets()
        self.resizable(width=False, height=False)
        
            
    def makewidgets(self):
        padding = {'padx' : 2, 'pady' : 2}
        textWidth = 2
        textHeight = 2
        textFont = ("Microsoft Sans Serif", 23, "bold")

        main_frame = Frame()
        main_frame.pack(anchor='center', padx=10, pady=10)
        main_frame.configure(background="#121213")

        labels = [[0 for j in range(5)] for i in range(6)]

        for i in range(len(labels)):
            for j in range(len(labels[i])):
                labels[i][j] = Frame(main_frame, height=62, width=62)
                labels[i][j].pack_propagate(0)
                labels[i][j].grid(row=i, column=j, **padding)
                Label(labels[i][j], text=f"{i + j}", font=textFont, background='#3A3A3C', foreground='#FFFFFF', borderwidth=0, width=4, height=2).pack(fill=BOTH, expand=1)

    def wordle(self, guess):
        with open('sgb-words.txt', 'r') as words:
            wordlist = words.read().splitlines()
            active_word = wordlist[randint(0, 1500)]




if (__name__ == "__main__"):
    app = App()
    app.mainloop()