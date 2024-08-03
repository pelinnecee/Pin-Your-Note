
import tkinter as tk
import tkinter.font as tkFont
def cli():
    import time
    current_time=time.strftime("%H:%M")
    print("Welcome to Pin your note application")
    time.sleep(2)
    note_input=input("Type your note here: ")
    note=("%s") % note_input
    time.sleep(1)

    root=tk.Tk()
    font = tkFont.Font(family="Times", size=12)

    def increase_font_size():
        font.config(size=font.actual()['size'] + 2)

    def decrease_font_size():
        font.config(size=max(8, font.actual()['size'] - 2))
    root.title("Pin your note")
    root.geometry("300x250")
    tk.Label(root,text=current_time,font=font).pack()
    tk.Label(root,text=note,bg="lightgray",fg="black",font=font).pack()
    increase_button = tk.Button(root, text="Increase Font Size", command=increase_font_size)
    increase_button.pack()

    decrease_button = tk.Button(root, text="Decrease Font Size", command=decrease_font_size)
    decrease_button.pack()
    root.mainloop()
cli()
