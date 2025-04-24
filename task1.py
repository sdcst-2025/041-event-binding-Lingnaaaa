import tkinter as tk 
from tkinter import *
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")

win=tk.Tk()
win.attributes('-topmost',True)
win.title("Sound Board")
win.geometry('580x250')


p1=PhotoImage(file="dog.png")
p1=p1.subsample(6,7)
l1=tk.Label(win,image=p1)
b1 =  tk.Button(win,text="Click to play")
b1.bind("<Button>",playsound)
l1.place(x=30,y=20)
b1.place(x=50,y=150)
l3=tk.Label(win,text="puppy",bg="cyan2").place(x=65,y=0)


def playsound2(event):
    print(event)
    p.playsound("cat-meow-8-fx-306184.mp3")

p2=PhotoImage(file="catt.png")
p2=p2.subsample(8,10)
l2=tk.Label(win,image=p2)
b2=tk.Button(win,text="Click to play")
b2.bind("<Button>",playsound2)
l2.place(x=200,y=20)
b2.place(x=220,y=150)
l4=tk.Label(win,text="Kitty",bg="cyan2").place(x=235,y=0)

def playsound3(event):
    print(event)
    p.playsound("cardinal-37075.mp3")

p3=PhotoImage(file="bird.png")
p3=p3.subsample(5,5)
l3=tk.Label(win,image=p3)
b3=tk.Button(win,text="Click to play")
b3.bind("<Button>",playsound3)
l3.place(x=380,y=20)
b3.place(x=400,y=150)
l5=tk.Label(win,text="bird",bg="cyan2").place(x=420,y=0)




win.mainloop()
