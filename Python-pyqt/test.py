import tkinter as tk
from tkinter import ttk

# create a new instance of the ttk.Style() class
style = ttk.Style()

# define the colors for the theme
style.configure('Custom.TButton', background='#3c3c3c',
                foreground='#ff0000', font=('Helvetica', 10, 'bold'))

# create a custom theme named 'custom_theme'
style.theme_create('custom_theme', parent='alt', settings={
    'TButton': {'configure': {'style': 'Custom.TButton'}}
})

# set the default theme to 'custom_theme'
style.theme_use('custom_theme')

# create a ttk.Button widget without specifying the style
button = ttk.Button(text='Click me!')
button.pack()

# start the tkinter event loop
root = tk.Tk()
root.mainloop()
