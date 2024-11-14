import tkinter as tk
import customtkinter as ctk

def say_hello():
    myInput = userInput.get()
    label.config(text = myInput)

if __name__ == "__main__":
	root = ctk.CTk()
	root.title("Button")
	root.geometry("300x100")

	userInput = ctk.CTkEntry(root, show="*")
	userInput.pack()
	
	button = ctk.CTkButton(root,
										text="Click Me!",
										command=say_hello)
	button.pack()

	label = ctk.CTkLabel(root,
									text="Hallo User")
	label.pack()

	root.mainloop()