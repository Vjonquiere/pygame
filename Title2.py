from tkinter import *
import variables
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Galaxy Wars")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.button = Button(master, text="Play", command=self.onClick())
        self.button.pack()

        self.nb_gouttes = IntVar()
        self.nb_gouttes_champs = Entry(master, textvariable=self.nb_gouttes, width=20)
        self.nb_gouttes_champs.pack()
        
    def onClick(self):
        try:
            a = int(self.nb_gouttes_champs.get())
            variables.valide = True
            print("t")
        except:
            variables.valide = False
        
        if variables.valide == True:
            print("hello")

root = Tk()
my_gui = GUI(root)
root.mainloop()
