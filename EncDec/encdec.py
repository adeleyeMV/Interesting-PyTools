#A encryption decryption program using GUI by sudoshivesh
import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()

pic = PhotoImage(file = "C:\\Users\\admin\\Desktop\\EncDec\\image\\images.png")
root.iconphoto(False,pic)
root.title("Text Encryptor-Decryptor")

root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

canvas = tk.Canvas(root,height = 500, width=400, bg="MediumPurple1")
canvas.pack()

bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")

label1 = tk.Label(root,text= "Enter the Text",width=20,bg="MediumPurple1")
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)

label2=tk.Label(root,text="Choose an Operation",width=25,bg="MediumPurple1")
label2.config(font=bold_font)
canvas.create_window(200,200,window=label2)

v = tk.IntVar()

def choice():
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

label3=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label3.config(font=bold_font)
canvas.create_window(100,250,window=label3)
label4=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label4.config(font=bold_font)
canvas.create_window(300,250,window=label4)

def encryption():
    plain_text = user_text.get()
    cipher_text = ""
    key = 3
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
            cipher_text+=chr((ord(letter)+key-97)%26+97)
    label5 =tk.Label(root,text=cipher_text,width=20,bg="light yellow")
    label5.config(font=bold_font)
    canvas.create_window(200,350,window=label5)

def decryption():
    cipher_text = user_text.get()
    plain_text = ""
    key = 3
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
            plain_text+=chr((ord(letter)-key-97)%26+97)
    label6 =tk.Label(root,text=plain_text,width=20,bg="light yellow")
    label6.config(font=bold_font)
    canvas.create_window(200,350,window=label6)

label7 =tk.Label(root,text="Converted Text ",width=20,bg="MediumPurple1")
label7.config(font=bold_font)
canvas.create_window(200,300,window=label7)

root.mainloop()
