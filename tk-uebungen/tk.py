import tkinter as tk

root = tk.Tk()
root.title("Hallo Tkinter")
#root.geometry("400x200")

label = tk.Label(root,
								text = "Hallo Label",
								bg="yellow",
								font=("Comic Sans MS", 15),
								wraplength=30,
								justify="right")
label.pack(padx=100, pady=50)

root.mainloop()