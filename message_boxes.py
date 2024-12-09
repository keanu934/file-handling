import tkinter as tk
from tkinter import messagebox

def show_message():
    response = messagebox.askyesno("Yes or No?", "Are we really doing this?")
    print(response)
    if response:
        print("We're doing this!")
    else:
        print("User wimped out")

        
window = tk.Tk()
window.title("Message Box")
window.geometry("400x300")

button = tk.Button(window,
                   text="Show message box",
                   command=show_message)


button.pack()
window.mainloop()