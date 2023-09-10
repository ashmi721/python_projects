from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="Blue")

lab = Label(sp,text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height= 50,width=380)

lab = Label(sp,text="Download Speed", font=("Time New Roman",20,"bold"))
lab.place(x=60,y=130,height= 50,width=380)

lab = Label(sp,text="00", font=("Time New Roman",20,"bold"))
lab.place(x=60,y=200,height= 50,width=380)

lab = Label(sp,text="Upload Speed", font=("Time New Roman",20,"bold"))
lab.place(x=60,y=290,height= 50,width=380)


lab = Label(sp,text="00", font=("Time New Roman",20,"bold"))
lab.place(x=60,y=360,height= 50,width=380)
button = Button(sp,text="Check Speed",font=('Time New Roman',30,"bold"),relief=RAISED,bg="red")
button.place(x=60,y=450,height=50,width=380)

sp.mainloop()