from tkinter import *
import tkinter as tk

expression = ''

def press(num):
    global expression
    expression += num
    label.config(text=expression)
 
def clear():
    global expression
    expression = ''
    label.config(text=expression)

def equalpress():
    global expression
    result = ''
    if expression != '':
        try:
            result = eval(expression)
        except:
            result = 'error'
            expression = ''
    label.config(text=result)         


root = tk.Tk()

root.geometry('300x400')
root.title('My Python Calculator')

label = tk.Label(root, text='', font=('Arial', 20))
label.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)

# Creating buttons
cls = tk.Button(buttonframe, text='C', relief=RAISED, bd=5, command=clear, fg='white', bg='blue', font=('Arial', 18))
cls.grid(row=0, column=0, columnspan=2, sticky=W+E)
div = tk.Button(buttonframe, text='/', relief=RAISED, bd=5, command=lambda: press('/'), fg='white', bg='black', font=('Arial', 18))
div.grid(row=0, column=2, sticky=W+E)
mod = tk.Button(buttonframe, text='%', relief=RAISED, bd=5, command=lambda: press('%'), fg='white', bg='black', font=('Arial', 18))
mod.grid(row=0, column=3, sticky=W+E)

btn1 = tk.Button(buttonframe, text='1', relief=RAISED, bd=5, command=lambda: press('1'), fg='white', bg='black', font=('Arial', 18))
btn1.grid(row=3, column=0, sticky=W+E)
btn2 = tk.Button(buttonframe, text='2', relief=RAISED, bd=5, command=lambda: press('2'), fg='white', bg='black', font=('Arial', 18))
btn2.grid(row=3, column=1, sticky=W+E)
btn3 = tk.Button(buttonframe, text='3', relief=RAISED, bd=5, command=lambda: press('3'), fg='white', bg='black', font=('Arial', 18))
btn3.grid(row=3, column=2, sticky=W+E)
plus = tk.Button(buttonframe, text='+', relief=RAISED, bd=5, command=lambda: press('+'), fg='white', bg='black', font=('Arial', 18))
plus.grid(row=3, column=3, sticky=W+E)

btn4 = tk.Button(buttonframe, text='4', relief=RAISED, bd=5, command=lambda: press('4'), fg='white', bg='black', font=('Arial', 18))
btn4.grid(row=2, column=0, sticky=W+E)
btn5 = tk.Button(buttonframe, text='5', relief=RAISED, bd=5, command=lambda: press('5'), fg='white', bg='black', font=('Arial', 18))
btn5.grid(row=2, column=1, sticky=W+E)
btn6 = tk.Button(buttonframe, text='6', relief=RAISED, bd=5, command=lambda: press('6'), fg='white', bg='black', font=('Arial', 18))
btn6.grid(row=2, column=2, sticky=W+E)
minus = tk.Button(buttonframe, text='-', relief=RAISED, bd=5, command=lambda: press('-'), fg='white', bg='black', font=('Arial', 18))
minus.grid(row=2, column=3, sticky=W+E)

btn7 = tk.Button(buttonframe, text='7', relief=RAISED, bd=5, command=lambda: press('7'), fg='white', bg='black', font=('Arial', 18))
btn7.grid(row=1, column=0, sticky=W+E)
btn8 = tk.Button(buttonframe, text='8', relief=RAISED, bd=5, command=lambda: press('8'), fg='white', bg='black', font=('Arial', 18))
btn8.grid(row=1, column=1, sticky=W+E)
btn9 = tk.Button(buttonframe, text='9', relief=RAISED, bd=5, command=lambda: press('9'), fg='white', bg='black', font=('Arial', 18))
btn9.grid(row=1, column=2, sticky=W+E)
multiply = tk.Button(buttonframe, text='*', relief=RAISED, bd=5, command=lambda: press('*'), fg='white', bg='black', font=('Arial', 18))
multiply.grid(row=1, column=3, sticky=W+E)

btn0 = tk.Button(buttonframe, text='0', relief=RAISED, bd=5, command=lambda: press('0'), fg='white', bg='black', font=('Arial', 18))
btn0.grid(row=4, column=0, sticky=W+E)
deci = tk.Button(buttonframe, text='.', relief=RAISED, bd=5, command=lambda: press('.'), fg='white', bg='black', font=('Arial', 18))
deci.grid(row=4, column=1, sticky=W+E)
equal = tk.Button(buttonframe, text='=', relief=RAISED, bd=5, command=equalpress, fg='white', bg='yellow', font=('Arial', 18))
equal.grid(row=4, column=2, columnspan=2, sticky=W+E)

buttonframe.pack(fill='y')
root.mainloop()
