import tkinter as tk

root = tk.Tk()
root.title("Textfeld")
root.geometry("450x120")

text = tk.Text(root,
               width=50,
               height=5)
text.pack(padx=10, pady=10)

root.mainloop()