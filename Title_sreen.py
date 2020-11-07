from tkinter import *
import variables
import game
from tkinter.font import Font

class Interface:
    
    def __init__(self, fenetre):    
 
        self.button = Button(fenetre, text="Play", command=self.onClick)
        self.button.pack()
        
        self.label = Label(fenetre, text="------Game-----")
        self.label.pack()
        
        self.nb_gouttes = IntVar()
        self.nb_gouttes_champs = Entry(fenetre, textvariable=self.nb_gouttes, width=20)
        self.nb_gouttes_champs.pack()
        
    def onClick(self):
        try:
            a = int(self.nb_gouttes_champs.get())
            variables.nb_gouttes = a
            game.real_game()
        except :
            print("You need to put a number")
        fenetre.destroy()
        
    def quit(self):
        global fenetre
        fenetre.quit()
fenetre = Tk()
interface = Interface(fenetre)


fenetre.mainloop()
