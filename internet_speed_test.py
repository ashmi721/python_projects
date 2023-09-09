from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="Blue")

lab = Label(sp,text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height= 50,width=380)

lab = Label(sp,text="Download Speed", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=130,height= 50,width=380)

lab = Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=200,height= 50,width=380)

lab = Label(sp,text="Upload Speed", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=290,height= 50,width=380)

lab = Label(sp,text="00", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=340,height= 50,width=380)

sp.mainloop()