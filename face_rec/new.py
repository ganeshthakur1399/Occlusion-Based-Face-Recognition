import tkinter as Snake_Game
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as t
import cv2
import numpy as np
from time import time
import random
import math
import os


def showMsg():  
    t.showinfo('About', 'You are playing the first ever human computer interaction based Snake Game')

def showMsg1():  
    t.showinfo('Help', 'How to play'.center(4) + '\n\n 1 . To play the game, just click on the New Game.'+ '\n 2 . Make sure your WebCam is working properly.' + '\n 3 . Take any red coloured object in front of the camera.' + '\n 4 . And just try to eat the apples appearing by moving the object.')

def run_prog():
    os.system('python detecting.py')

wnd = Snake_Game.Tk()

wnd.geometry("{0}x{1}+0+0".format(wnd.winfo_screenwidth(), wnd.winfo_screenheight()))

bg = Image.open("SnakeGame.jpg")
new_img = bg.resize((1600,820))
bg1 = ImageTk.PhotoImage(new_img)

start_img = Image.open("start_game.jpg")
new_img = start_img.resize((170,50))
start_image = ImageTk.PhotoImage(new_img)

exit_img = Image.open("end_game.jpg")
new_img1 = exit_img.resize((170,50))
exit_image = ImageTk.PhotoImage(new_img1)

canvas = Canvas(wnd, width=1920,height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, anchor="nw",image=bg1)

canvas.create_text(450,100,text = "Snake Game",font=("Helvetica",80), fill="white" ) 

btn = Snake_Game.Button(wnd, image=start_image, height =50, width=170, bd = 0, relief = "flat" ,command = run_prog)
btn.pack()
btn.place(relx=0.20,rely=0.35)

btn = Snake_Game.Button(wnd, image=exit_image, height =50, width=170, bd = 0, relief = "flat" ,command = wnd.destroy)
btn.pack()
btn.place(relx=0.20,rely=0.45)

btn1 = Snake_Game.Button(wnd,text = "About",fg = 'white', bd=4,font=("Helvetica",13),relief ="raised",height =1,width=10,activebackground = "White",bg='#237d2b',command = showMsg)
btn1.pack()
btn1.place(x=1210, y=650)

btn2 = Snake_Game.Button(wnd,text = "Help",bd=4,fg = 'white',font=("Helvetica",13),relief ="raised",height =1,width=10,activebackground = "White",bg='#237d2b',command = showMsg1)
btn2.pack()
btn2.place(x=1100, y=650)

wnd.mainloop()