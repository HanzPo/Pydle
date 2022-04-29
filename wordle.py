from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
from random import randint

class App(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title("Wordle")
        with open('sgb-words.txt', 'r') as words:
            wordlist = words.read().splitlines()
            active_word = wordlist[randint(0, 1500)]
            print(active_word)


if (__name__ == "__main__"):
    app = App()
    app.mainloop()