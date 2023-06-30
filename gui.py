from tkinter import *
from PIL import Image, ImageTk
import wordModule as mod
import sys

window = Tk()
window.resizable(0,0)

# Grabs user word
def action():
    global usr_word
    usr_word = txtfld1.get()

# Delete entry field text "Quaero" when user types
def temp_text(e):
   txtfld1.delete(0, "end")

# Creates new window with dictionary entry for user-searched word
def dictionary_window():
    window2 = Toplevel()

    window2.title("Julius: A Latin Dictionary")
    window2.geometry("600x400+10+10")

    definition = word_definition()
    etymology = word_etymology()
    synonyms = word_synonyms()

    try:
        # DEFINITION
        if definition[0] != TypeError:
            lb2 = Text(window2,height=100, width=100)
            lb2.pack(pady=10)
            lb2.insert(END, definition[0] + "\n\n")
            #lb2.insert(END, "Definition:\n")
            if not synonyms:
                for item in definition[1:]:
                    lb2.insert(END, "* " + item + "\n")
            else:
                for item, synonym in zip(definition[1:], synonyms):
                    lb2.insert(END, "* " + item + "\n")
                    lb2.insert(END, "\t" + synonym + "\n")
            # ETYMOLOGY
            #lb2.insert(END, "\nEtymology:\n")
            lb2.insert(END, "\n\n" + etymology + "\n")
        lb2.config(state=DISABLED)
    except TypeError:
        # 404 IMAGE 
        image404 = Image.open("images/dead_caesar.png")
        resize_image404 = image404.resize((125, 125))
        image404_resized = ImageTk.PhotoImage(resize_image404)
        image_lbl404 = Label(window2, image=image404_resized)
        image_lbl404.image = image404_resized
        image_lbl404.place(relx=0.5, rely=0.3, anchor=CENTER)
        # 404 TEXT
        error_main = Label(window2, text="CDIV", font=("Times new roman", 35))
        error_main.place(relx=0.5, rely=0.6, anchor=CENTER)
        error_sub = Label(window2, text="TRY SEARCHING AGAIN...", font=("arial italic", 15))
        error_sub.place(relx=0.5, rely=0.725, anchor=CENTER)
        
    window2.mainloop()

def word_definition():
    word_object = mod.Word(usr_word.lower())
    definition = word_object.getDefinition()
    return definition

def word_etymology():
    word_object = mod.Word(usr_word.lower())
    etymology = word_object.getEtymology()
    return etymology
def word_synonyms():
    word_object = mod.Word(usr_word.lower())
    synonyms = word_object.getSynonyms()
    return synonyms

# POP UP DICTIONARY WINDOW WHEN USER ENTERS WORD
def dictionaryAction(event):
    action()
    dictionary_window()

# Main Body
window.title("Julius: A Latin Dictionary")
window.geometry("600x400+10+10")
    
# IMAGE
image1 = Image.open("images/column_julius.webp")
resize_image = image1.resize((400, 400))
image_resized = ImageTk.PhotoImage(resize_image)

image_lbl1 = Label(image=image_resized)
image_lbl1.image = image_resized
image_lbl1.place(relx=0.5, rely=1.0, anchor=CENTER)

# TITLE
text_lbl0 = Label(window, text="JULIUS", font=("Times new roman", 50))
text_lbl0.place(relx=0.5, rely=0.2, anchor=CENTER)
# SUBTITLE
text_lbl1 = Label(window, text="A LATIN DICTIONARY", font=("Times new roman", 10))
text_lbl1.place(relx=0.5, rely=0.31, anchor=CENTER)
# CREDIT
text_lbl2 = Label(window, text="Built using Wiktionary", font=("helvetica", 10))
text_lbl2.place(x=485, y=375)

# TEXT ENTRY FIELD
txtfld1=Entry(window, text="", bd=1, justify=CENTER)
txtfld1.place(relx=0.5, rely=0.425, anchor=CENTER)
txtfld1.insert(0, "Quaero")
txtfld1.bind("<FocusIn>", temp_text)

window.bind('<Return>', dictionaryAction)

window.mainloop()


