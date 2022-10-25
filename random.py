from tkinter import *
import random

root = Tk()
root.title("Random Color")
root.geometry("600x600")
root.config(bg="Slate Gray1")

color = Label(root,font=("Sylfaen",25),bg="Slate Gray1")
color.place(relx=0.5,rely=0.2,anchor=CENTER)

class game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["red","green","blue","yellow","pink","purple","orange","brown","black"]
        self.random_num_for_text = random.randint(0,8)
        self.color = ["red","green","blue","yellow","pink","purple","orange","brown","black"]
        self.random_num_for_color = random.randint(0,8)
        
        color["text"]=self.text[self.random_num_for_text]
        color["fg"]=self.color[self.random_num_for_color]

obj = game()

btn = Button(root,text="Start",command=obj.updateGame,bg="SteelBlue1",relief=FLAT,padx=5,pady=5)
btn.place(relx=0.5,rely=0.5,anchor=S)
root.mainloop()