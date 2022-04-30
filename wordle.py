from tkinter import *
from random import randint

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordle")
        self.resizable(width=False, height=False)
        self.configure(background="#121213")
        self.guess_number = 0
        self.character_number = 0
        self.characters = [[' ' for j in range(5)] for i in range(6)]
        self.frames = [[0 for j in range(5)] for i in range(6)]
        self.labels = [[0 for j in range(5)] for i in range(6)]
        self.bind("<Key>", self.key_pressed)
        self.makewidgets()
            
    def makewidgets(self):
        padding = {'padx' : 2, 'pady' : 2}
        textWidth = 4
        textHeight = 2
        textFont = ("Microsoft Sans Serif", 23, "bold")

        main_frame = Frame()
        main_frame.pack(anchor='center', padx=10, pady=10)
        main_frame.configure(background="#121213")

        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])):
                self.frames[i][j] = LabelFrame(main_frame, height=62, width=62, borderwidth=0)
                self.frames[i][j].pack_propagate(0)
                self.frames[i][j].grid(row=i, column=j, **padding)
                self.labels[i][j] = Label(self.frames[i][j], text=f"{self.characters[i][j]}", font=textFont, background='#3A3A3C', foreground='#FFFFFF', borderwidth=0, width=textWidth, height=textHeight)
                self.labels[i][j].pack(fill=BOTH, expand=1)

    def key_pressed(self, event):
        with open('sgb-words.txt', 'r') as words:
            wordlist = words.read().splitlines()
            active_word = wordlist[randint(0, 1500)]
            allowed_keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            pressed_key = event.char
            if (self.character_number < 5 and pressed_key.upper() in allowed_keys):
                self.characters[self.guess_number][self.character_number] = pressed_key.upper()
                self.character_number += 1
            elif (event.keysym == 'BackSpace' and self.character_number > 0):
                self.character_number -= 1
                self.characters[self.guess_number][self.character_number] = " "
            elif (self.character_number == 5 and event.keysym == 'Return'):
                current_word = ''.join(self.characters[self.guess_number]).lower()
                if (current_word in wordlist):
                    for i in range(len(current_word)):
                        if current_word[i] == active_word[i]:
                            self.labels[self.guess_number][i].config(background='#538d4e')
                        elif (current_word[i] in active_word):
                            self.labels[self.guess_number][i].config(background='#b59f3b')

                    self.guess_number += 1
                    self.character_number = 0
                else:
                    self.open_popup(current_word)
            self.update_chars()

    def update_chars(self):
        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])):
                self.labels[i][j].config(text=f"{self.characters[i][j]}")

    def open_popup(self, invalid_word):
        textFont = ("Microsoft Sans Serif", 16)
        popup = Toplevel(self, background="#121213")
        popup.attributes('-toolwindow', True)
        Label(popup, text= f"{invalid_word} is not in the wordlist", font=textFont, background="#121213", foreground='#FFFFFF').pack(padx=5, pady=5)





if (__name__ == "__main__"):
    app = App()
    app.mainloop()