import tkinter as tk
from tkinter import *
from PIL import ImageTk
import books
import gen

# creates an instance of Tkinter frame
window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

# defines geometry
window.geometry(str(width) + "x" + str(height))
window.title("illustrAItor")

# Tittle label
labelT = tk.Label(window, text="illustrAItor", font=('Arial', 24))
labelT.pack(padx=20)

# Slogan label
labelS = tk.Label(window, text="Making every book a picture book with A.I.", font=('Arial', 14))
labelS.pack(padx=20, pady=7)

styleLabel = tk.Label(window, text="Generate images in the style of...", font=('Arial', 14))

#  Style modifier
styleLabel.place(relx=0.05, rely=0.85)
styleBox = tk.Entry(window, bd=1)
styleBox.place(relx=0.05, rely=0.9)

titles = books.get_titles()

# Dropdown menu options
clicked = StringVar()

global v
v = StringVar()
label1 = tk.Label(window, textvariable=v, font=('Arial', 22), justify=LEFT, wraplength=500)
label1.place(relx=0.05, rely=0.45, anchor=W)


def make_pic(selection):
    b = selection
    s = styleBox.get()
    if s == "":
        s = "painting"
    v.set(books.get_book_by_title(b))
    for i in range(3):
        p = books.get_best_sentences(selection)[i]
        img = (ImageTk.PhotoImage(gen.make_image(b, p, s)))
        label2 = tk.Label(image=img)
        label2.image = img
        label2.place(relx=0.70, y=(250 * i) + 10)


# datatype of menu text
clicked.set(titles[0])
# initial menu text
drop = OptionMenu(window, clicked, *titles, command=make_pic)
# Create Dropdown menu
drop.pack()
window.mainloop()
