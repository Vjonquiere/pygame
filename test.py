from tkinter import *
import variables
import game
import pyglet, os

pyglet.font.add_file('ConcertOne-Regular.ttf')

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Galaxy Wars")
        self.master.geometry('500x300')
        self.color_back = "#0F4C81"
        self.master.configure(background = self.color_back)
        
        ##### txt attributs ##############################################################################################################################################################################################################
        ##### magic command : background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background  ###
        self.highlightbackground = "#162a3a" 
        self.relief = "flat"
        self.foreground = "#162a3a"
        self.background = "#0F4C81"
        self.font = "Concert One"
        ###################################################################################################################################################################################################################################
        ###################################################################################################################################################################################################################################
        self.label = Label(self.master, text="Welcome to Galaxy War", font=(self.font, 25), background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background,width=20, height=2)
        self.label.grid(pady=10, column = 1, row = 1)

        self.close_button = Button(self.master,background = self.color_back, text="Close", command=master.quit, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background )
        self.close_button.grid(pady=10, column = 1, row = 4)
        
        self.goutte_champs_label = Label(self.master, text="please enter an objective :",font=(self.font, 18), background = "blue", highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background, pady=10)
        self.goutte_champs_label.grid(pady=5, column = 1, row = 2)
        
        self.max_gouttes = 100
        self.nb_gouttes = IntVar()
        self.nb_gouttes_champs = Entry(master, textvariable=self.nb_gouttes, background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, width=5)
        self.nb_gouttes_champs.grid(pady=10, column = 2, row = 2)

        self.player_champs_label = Label(self.master, text="please enter a number player :",font=(self.font, 18),  background = "blue", highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background,pady=10)
        self.player_champs_label.grid(pady=10, padx = 2, column = 1, row = 3)
        
        self.max_player = 2
        self.nb_player = IntVar()
        self.nb_player_champs = Entry(master, textvariable=self.nb_player,background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, width=5)
        self.nb_player_champs.grid(padx=10, column = 2, row = 3)
        
        self.greet_button = Button(master, text="Play", command=self.onClick, background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background, height=2, width=7)
        self.greet_button.grid(pady=10, column = 2, row = 4)
  
        
    def onClick(self):
        try:
            a = int(self.nb_gouttes_champs.get())
            variables.valide = True
        except:
            variables.valide = False
            self.error_message("Ball number must be an number !")
            
        try:
            n = int(self.nb_player_champs.get())
            variables.valide = True
        except:
            variables.valide = False
            self.error_message("You can't play with no player !")
            
        if variables.valide and a != 0 and a<= self.max_gouttes and n != 0 and n <= self.max_player:
            print("hello")
            print(a)
            variables.nb_gouttes = a
            game.launch_game()
        else:
            self.error_message("You can't play with 0 ball")
            
    def error_message(self, error):
        self.error = error
        self.error_mes = Label(self.master, text=self.error)
        self.error_mes.pack()
        
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
