''' This project is a simple English to Nepali dictionary built using the 'tkinter' library
for creating a graphical user interface (GUI) & the google Translate API translation for translate 
English meaning to Nepali.
'''

# for a gui interface
import tkinter as tk  
 # for use the google Translator Api
from googletrans import Translator

# create a Translator instance
translator = Translator()

# funtion to translate english to nepali using the google translate API
def translate_to_nepali():
    word_to_translate = entry.get()
    translation = translator.translate(word_to_translate, src='en',dest='ne')
    translated_word.set(translation.text)

# function to clear the user previous input automatically
def clear_input():
    entry.delete(0,tk.END)    
# create the main Gui window
root = tk.Tk()
root.title("English to Nepali Dictinary")

# Create a label
label = tk.Label(root,text='Enter an English word:')
label.pack()

# Create an entry widget for user input'
entry = tk.Entry(root,width=49)
entry.pack()

# Create a button to trigger translation
translate_button = tk.Button(root, text = "Search",width=9,height=1, command=translate_to_nepali)
translate_button.pack()

# Create a clear button
clear_button = tk.Button(root, text="Clear",width=9,height=1, command=clear_input)
clear_button.pack()

# Create a label to display the translated word
translated_word = tk.StringVar()
result_label = tk.Label(root,textvariable=translated_word)
result_label.pack()



root.mainloop()