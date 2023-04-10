from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


def select_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((180, 180), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(image=img)
    label.image = img
    label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


def hide_message():
    # Code to hide message in image goes here
    pass


def read_message():
    # Code to read message from image goes here
    pass


root = Tk()
root.title("Hide message in image")
root.geometry("500x500")

button_select = Button(text="Select image", command=select_image)
button_select.grid(row=0, column=0, pady=5)

mode_label = Label(text="Select mode:")
mode_label.grid(row=0, column=1)

mode_var = StringVar()
mode_var.set("read")

hide_button = Radiobutton(text="Hide message", variable=mode_var, value="hide")
hide_button.grid(row=0, column=2, padx=5)

read_button = Radiobutton(text="Read message", variable=mode_var, value="read")
read_button.grid(row=0, column=3)

message_label = Label(text="Enter message:")
message_label.grid(row=2, column=0, pady=5)

message_entry = Entry(width=50)
message_entry.grid(row=2, column=1, columnspan=2)

button_hide = Button(text="Hide message", command=hide_message)
button_hide.grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()
