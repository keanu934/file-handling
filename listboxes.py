import tkinter as tk


def add_character():
    item = entry.get().strip()
    if item and not item in listbox.get(0,tk.END):
        listbox.insert(tk.END, item)

def remove_selected():
    for_del = listbox.get(tk.ACTIVE)
    if for_del:
        listbox.delete(tk.ACTIVE)
        print(f"deleted {for_del}")
        print(f"current active: {listbox.get(tk.ACTIVE)}")


window = tk.Tk()
window.title("Marion Characters")
window.geometry("400x400")

listbox = tk.Listbox(window,  width=25, height= 8)
listbox.pack()

listbox.insert(0,"Mario")
listbox.insert(1,"Luigi")
listbox.insert(2,"Princess Peach")
print(f"current active: {listbox.get(tk.ACTIVE)}")
listbox.select_set(1)



entry= tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Add Character", command=add_character)
button.pack()


button_del = tk.Button(window, text="Remove Selected",
                       command=remove_selected)
button_del.pack()

window.mainloop()
