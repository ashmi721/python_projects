from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="Blue")

lab = Label(sp,text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=70,y=30)

lab = Label(sp,text="Download Speed", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=70,y=70)

sp.mainloop()