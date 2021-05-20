from tkinter import *
import variables
import game
import pyglet, os, time

pyglet.font.add_file('ConcertOne-Regular.ttf')

class GUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Galaxy Wars")
        self.master.geometry('700x350')
        self.master.maxsize(700, 350)
        self.master.minsize(700, 350)
        self.color_back = "#0F4C81"
        self.master.configure(background = self.color_back)
        self.master.columnconfigure(1,pad = 10,minsize= 500)
        self.master.rowconfigure(1,weight=0, minsize=100)
  
        
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

        
        self.goutte_champs_label = Label(self.master, text="please enter an objective :",font=(self.font, 18), background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background, pady=10)
        self.goutte_champs_label.grid(pady=5, column = 1, row = 2)
        
        self.max_objectifs = 100
        self.nb_objectifs = IntVar()
        self.nb_objectifs_champs = Entry(master, textvariable=self.nb_objectifs, background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, width=5)
        self.nb_objectifs_champs.grid(pady=(25,0) , column = 2, row = 2)

        self.player_champs_label = Label(self.master, text="please enter a number player :",font=(self.font, 18),  background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background,pady=10)
        self.player_champs_label.grid(pady=10, padx = 2, column = 1, row = 3)
        
        self.max_player = 2
        self.nb_player = IntVar()
        self.nb_player_champs = Entry(master, textvariable=self.nb_player,background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, width=5)
        self.nb_player_champs.grid(column = 2, row = 3,pady=(25,0))
        
        self.greet_button = Button(master, text="Play", command=self.onClickPlay, background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground=self.foreground, activebackground=self.highlightbackground, activeforeground=self.background, height=2, width=7)
        self.greet_button.grid(pady=(25,0), column = 2, row = 4)
        
        self.error = ""
       
    def onClickPlay(self):
        
        # checking if input are INT
        try:
            a = int(self.nb_objectifs_champs.get())
            variables.objectif_valide = True
        except:
            variables.objectif_valide = False
            
        try:
            n = int(self.nb_player_champs.get())
            variables.player_valide = True
        except:
            variables.player_valide = False
            
        # All requirements to play 
        if variables.objectif_valide :
            if a != 0:
                if a<= self.max_objectifs:
                    if variables.player_valide :
                        if n != 0:
                            if n <= self.max_player:
                                variables.nb_player = n
                                variables.nb_objectifs = a
                                game.launch_game()
                            else:
                                self.error_message("2 players max")
                        else:
                            self.error_message("You need a player to play")
                    else:
                        self.error_message("You can't play with no player !")
                else:
                    self.error_message("You must play with a possible ojective") 
            else:
                self.error_message("You can't play with 0 ball")
        else:
            print("hr")
            self.error_message("Ball number must be an number !")
            
    def error_message(self, error):
        if self.error != "":
            self.error_mes.grid_remove()
        self.error = error
        self.error_mes = Label(self.master, text=self.error, font=(self.font, 12), background = self.color_back, highlightbackground=self.highlightbackground, relief=self.relief, foreground="#7e1818", activebackground=self.highlightbackground, activeforeground=self.background,width=20, height=2)
        self.error_mes.grid(column=1, row= 5)


 
root = Tk()
my_gui = GUI(root)
root.mainloop()
