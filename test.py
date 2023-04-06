from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Hide message in image")
root.geometry("500x500")

# functions


def select_image():
    global img_path, img_label, img
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[
                                          ("PNG", "*.png"), ("JPEG", "*.jpg")])
    if img_path:
        img = Image.open(img_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img


def hide_message():
    global img_path, img_label, img
    # remove second button and show message input field
    hide_btn.pack_forget()
    read_btn.pack_forget()
    message_entry.pack()


def read_message():
    global img_path, img_label, img
    # remove message input field and show second button
    message_entry.pack_forget()
    hide_btn.pack()
    read_btn.pack()


def hide_message_in_image():
    global img_path, img_label, img
    message = message_entry.get()
    if message:
        img = Image.open(img_path)
        pixels = img.load()
        width, height = img.size
        message += "~"  # add delimiter to mark end of message
        binary_message = ''.join([format(ord(i), "08b") for i in message])
        index = 0
        for i in range(height):
            for j in range(width):
                r, g, b = pixels[j, i]
                if index < len(binary_message):
                    pixels[j, i] = (r - r % 2 + int(binary_message[index]), g - g % 2 + int(
                        binary_message[index+1]), b - b % 2 + int(binary_message[index+2]))
                    index += 3
                else:
                    img_label.config(text="Message hidden successfully!")
                    img.save(filedialog.asksaveasfilename(
                        defaultextension=".png", filetypes=[("PNG", "*.png")]))
                    return
        img_label.config(text="Insufficient pixels to hide message!")
    else:
        img_label.config(text="Please enter a message to hide!")


# widgets
img_label = Label(root, width=300, height=300)
img_label.pack(pady=10)

select_btn = Button(root, text="Select Image", command=select_image)
select_btn.pack()

message_entry = Entry(root, width=50)
hide_btn = Button(root, text="Hide Message", command=hide_message)
read_btn = Button(root, text="Read Message", command=read_message)

# display widgets
read_btn.pack()
root.mainloop()
