import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

def say_hello():
	label.config(text="Tschüß")

if __name__ == "__main__":
	root = ctk.CTk()
	root.title("Button")
	root.geometry("300x100")

	button = ctk.CTkButton(root,
										text="Click Me!",
										command=say_hello)
	button.pack()

	label = tk.Label(root,
									text="Hallo User")
	label.pack()

	root.mainloop()