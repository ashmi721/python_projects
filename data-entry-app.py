import tkinter as tk
'''This is a GUI application that allows users to input their data and then save 
that data to a text file when they click the "Save" button'''
# define the funtion\
def save_data():
    name = name_entery.get()
    age = age_entery.get()
    email = email_entery.get()
    address = address_entery.get()
   
   # save the data in the file
    with open("data.txt", "a") as file:
        file.write(f"Name:{name}, Age:{age}, Email:{email}, Address: {address}\n")

    # clear the text field after save the data
    name_entery.delete(0,tk.END)
    age_entery.delete(0,tk.END)
    email_entery.delete(0,tk.END)
    address_entery.delete(0,tk.END)
app = tk.Tk()
app.title("Data Entery Application")
# label
tk.Label(app, text='Name:').grid(row=0,column=0,padx=10,pady=5)
tk.Label(app, text='Age:').grid(row=1,column=0,padx=10,pady=5)
tk.Label(app, text='Email:').grid(row=2,column=0,padx=10,pady=5)
tk.Label(app, text='Address:').grid(row=3,column=0,padx=10,pady=5)

# creating entry field
name_entery = tk.Entry(app)
name_entery.grid(row=0,column=1,padx=10,pady=5)

age_entery = tk.Entry(app)
age_entery.grid(row=1,column=1,padx=10,pady=5)
email_entery = tk.Entry(app)
email_entery.grid(row=2,column=1,padx=10,pady=5)
address_entery = tk.Entry(app)
address_entery.grid(row=3,column=1,padx=10,pady=5)

# creating a save button
save_button = tk.Button(app,text="Save",command=save_data)
save_button.grid(row=5,column=0,columnspan=2,padx=10,pady=5)
app.mainloop()