from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    try:
        down = str(round(sp.download() / (10**6), 3)) + "Mbps"
        up = str(round(sp.upload() / (10**6), 3)) + "Mbps"
        lab_down.config(text=down)
        lab_up.config(text=up)
    except Exception as e:
        lab_down.config(text="Error: " + str(e))
        lab_up.config(text="Error: " + str(e))

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="Blue")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman", 20, "bold"))
lab.place(x=60, y=130, height=50, width=380)
lab_down = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 20, "bold"))
lab.place(x=60, y=290, height=50, width=380)
lab_up = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="Check Speed", font=('Time New Roman', 30, "bold"), relief=RAISED, bg="Red", command=speedcheck)
button.place(x=60, y=450, height=50, width=380)

sp.mainloop()
