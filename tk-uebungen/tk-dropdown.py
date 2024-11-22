import tkinter as tk
from tkinter import ttk

def change_color():
    text.config(bg=color.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dropdown")
    root.geometry("800x450")

    color = tk.StringVar()

    text = tk.Text(root,
                   width=100,
                   height=10)
    text.pack(pady=10)

    colors = [
        "yellow",
        "blue",
        "green",
        "red"
    ]

    dropdown = ttk.Combobox(root,
                            textvariable=color,
                            values=colors,
                            state="readonly",
                            width=18,
                            font=("Verdana", 12))
    dropdown.pack()

    tk.Button(root,
              text="Farbe ändern",
              command=change_color).pack(pady=10)
    
    root.mainloop()