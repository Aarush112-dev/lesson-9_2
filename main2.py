from tkinter import *
import random
from tkinter import messagebox

window=Tk()
window.title('Jumbled words game')
window.geometry("400x400")
window.config(background="black")

jumbled_word_game = Label(window,text="JUMBLED WORD GAME",background="black",fg="white",font=("Aerial",16))
jumbled_word_game.pack(side=TOP)

jumbled_word = Label(window,text="",background="black",fg="white",font=("Aerial",8))
jumbled_word.place(x=175,y=100)

enter_word = Entry(window,width=30)
enter_word.place(x=105,y=150,height=30)

check_button = Button(window,text="Check")
reset_button = Button(window,text="Reset")
check_button.place(x=175,y=200)
reset_button.place(x=175,y=250)





window.mainloop()