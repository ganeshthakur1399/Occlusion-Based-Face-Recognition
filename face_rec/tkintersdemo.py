from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
import tkinter.filedialog as tkFileDialog
import cv2

def my_function():
    os.system('python face_recognition.py')
    


window = Tk()
window.title('Occlusion based Face Recognition Model')
window.geometry("600x400")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

bg = Image.open("SnakeGame.jpg")
new_img = bg.resize((1600,820))
bg1 = ImageTk.PhotoImage(new_img)

text = Text(window)
text.insert(INSERT, "\n\tWelcome to Occlusion based Face Recognition Model")
text.insert(END, "")
text.pack()

text.tag_add("Write Here", "1.0", "1.50")
text.tag_config("Write Here", background="yellow", foreground="black")

btn = Button(window, text="Let's get started", fg='blue', command=my_function)
btn.place(x=250, y=200)
window.mainloop()