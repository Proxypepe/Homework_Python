from tkinter import *
from tkinter.ttk import *


def clicked():
    msg = f"Text {ent.get()}"
    lbl.configure(text=msg)


if __name__ == '__main__':
    window = Tk()
    window.title("Alex")
    window.geometry("500x200")
    lbl = Label(
        window,
        text="Hello, world!",
        font=("Arial Bold", 50)
    )
    btn = Button(
        window,
        text="OK",
        command=clicked
    )
    ent = Entry(window, width=10)
    combo = Combobox(window)
    combo['values'] = (1, 2, 3, 4, 5)
    combo.current(1)
    chk_state = BooleanVar()
    chk_state.set(True)
    chk = Checkbutton(window, text="Choose", variable=chk_state)
    Radiobutton(window, text="First", value=1).grid(column=0, row=3)
    Radiobutton(window, text="Second", value=2).grid(column=0, row=4)
    Radiobutton(window, text="Third", value=3).grid(column=0, row=5)
    lbl.grid(column=0, row=0)
    btn.grid(column=0, row=1)
    ent.grid(column=1, row=1)
    combo.grid(column=0, row=2)
    chk.grid(column=1, row=2)
    window.mainloop()
