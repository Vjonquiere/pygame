from tkinter import *
import variables
import game
from tkinter.font import Font

class Interface(Frame):
    
    def __init__(self, fenetre, **kwargs):    
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        
        self.button = Button(fenetre, text="Play", command=self.change())
        self.button.pack()
        
        self.mes = "message 1"
        self.label = Label(fenetre, text=self.mes)
        self.label.pack()
        
        self.error_mes = "k"
        self.error_message = Label(fenetre, text=self.error_mes)
        self.error_message.pack()
        
        self.nb_gouttes = IntVar()
        self.nb_gouttes_champs = Entry(fenetre, textvariable=self.nb_gouttes, width=20)
        self.nb_gouttes_champs.pack()
        
    def onClick(self):
        try:
            a = int(self.nb_gouttes_champs.get())
            if a != 0 :     
                variables.nb_gouttes = a
                game.real_game()
                if variables.quit != 1:
                    print("sd")
            else:
                self.error_mes = "You can't play with 0 ball"
                self.error_message["text"] = "You can't play with 0 ball"
                
            
        except :
            self.error_mes = "You need to put a number"
            

    def change(self):
        self.mes = "dusnufins"
        
    def quit(self):
        global fenetre
        fenetre.quit()
        
fenetre = Tk()
interface = Interface(fenetre)


interface.mainloop()
