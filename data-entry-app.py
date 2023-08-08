import tkinter as tk
'''This is a GUI application that allows users to add,view and search the related data
which  data store in a text file when they click the "Save" button'''
app = tk.Tk()
app.title("Medicine Management System")

def add_medicine():
    name = name_entry.get()
    quantity = quantity_entry.get()
    manufacture = manufacture_entry.get()
    expiration_date = expire_entry.get()

    with open("medicines.txt", "a") as file:
        file.write(f"{name},{quantity},{manufacture},{expiration_date}\n")

    print("Medicine added successfully!")
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    manufacture_entry.delete(0, tk.END)
    expire_entry.delete(0, tk.END)

def view_medicines():
    view_window = tk.Toplevel(app)
    view_window.title("View Medicines")
    text_widget = tk.Text(view_window)
    text_widget.pack(padx=10, pady=10)

    with open("medicines.txt", "r") as file:
        medicines = file.readlines()
        for idx,medicine in enumerate(medicines,start=1):
            text_widget.insert(tk.END,medicine)
            
def search_medicine():
    search_term = search_entry.get().lower()  # Get the search term from the entry field

    search_results = []  # To store matching medicines

    with open("medicines.txt", "r") as file:
        medicines = file.readlines()
        for medicine in medicines:
            values = medicine.strip().split(',')
            if len(values) == 4:  # Check if the line contains all four values
                name, quantity, manufacture, expiration_date = values
                if search_term in name.lower():
                    search_results.append((name, quantity, manufacture, expiration_date))

    if search_results:
        search_window = tk.Toplevel(app)
        search_window.title("Search Results")
        text_widget = tk.Text(search_window)
        text_widget.pack(padx=10, pady=10)

        for idx, (name, quantity, manufacture, expiration_date) in enumerate(search_results, start=1):
            result_text = f"{idx}. Name: {name}, Quantity: {quantity}, Manufacture: {manufacture}, Expiration Date: {expiration_date}\n"
            text_widget.insert(tk.END, result_text)
    else:
        print("No matching medicines found.")




# Labels and entry fields for adding medicines
tk.Label(app, text="Medicine_Name:").grid(row=0, column=0, padx=10, pady=7)
tk.Label(app, text="Quantity:").grid(row=1, column=0, padx=10, pady=7)
tk.Label(app, text="Manufacture:").grid(row=2, column=0, padx=10, pady=7)
tk.Label(app, text="Expiration_date:").grid(row=3, column=0, padx=10, pady=7)

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=7)
quantity_entry = tk.Entry(app)
quantity_entry.grid(row=1, column=1, padx=10, pady=7)
manufacture_entry = tk.Entry(app)
manufacture_entry.grid(row=2, column=1, padx=10, pady=7)
expire_entry = tk.Entry(app)
expire_entry.grid(row=3, column=1, padx=10, pady=7)

# Button to add medicine
add_button = tk.Button(app, text='Add', command=add_medicine)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=7)

# Button to view medicines
view_button = tk.Button(app, text='View Medicines', command=view_medicines)
view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=7)

# lable and entry field for search medicine
tk.Label(app, text="Search Term:").grid(row=7, column=0, padx=10, pady=7)
search_entry = tk.Entry(app)
search_entry.grid(row=7, column=1, padx=10, pady=7)

# Button to initiate search
search_button = tk.Button(app, text='Search', command=search_medicine)
search_button.grid(row=8, column=0, columnspan=2, padx=10, pady=7)

app.mainloop()
