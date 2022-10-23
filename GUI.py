import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import books
import gen

# creates an instance of Tkinter frame
window = tk.Tk()
`~
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

# Print the screen size
print("Screen width:", width)
print("Screen height:", height)

# defines geometry
window.geometry(str(width) + "x" + str(height))
# window.attributes('-fullscreen', True)
window.title("illustrAItor")

# Tittle label
labelT = tk.Label(window, text="illustrAItor", font=('Arial', 24))
labelT.pack(padx=20)

# Slogan label
labelS = tk.Label(window, text="Making every book a picture book", font=('Arial', 14))
labelS.pack(padx=20, pady=7)


styleLabel = tk.Label(window, text="Generate images in the style of...", font=('Arial', 14))

#  Style modifier
styleLabel.place(relx=0.05, rely=0.85)
styleBox = tk.Entry(window, bd=1)
styleBox.place(relx=0.05, rely=0.9)

titles = books.get_titles()

# Dropdown menu options
clicked = StringVar()



def make_pic(selection):
    b = selection
    s = styleBox.get()
    p = books.get_best_sentences(selection)[0]
    if s == "":
        s = "painting"
    print(b)
    print(p)
    print(s)
    img = ImageTk.PhotoImage(gen.make_image(b, p, s))
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(relx= 0.2, rely=0.2)

# datatype of menu text
clicked.set(titles[0])
# initial menu text
drop = OptionMenu(window, clicked, *titles, command=make_pic)
# Create Dropdown menu
drop.pack()

# button = tk.Button(window, text="Generate!", font=('Arial', 18), command=make_pic)
# button.place(relx=0.5, rely=0.9,anchor=N)

window.mainloop()
