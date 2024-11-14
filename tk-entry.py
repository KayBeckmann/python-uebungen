import tkinter as tk

def say_hello():
    myInput = userInput.get()
    label.config(text = myInput)

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Button")
	root.geometry("300x100")

	userInput = tk.Entry(root, show="*")
	userInput.pack()
	
	button = tk.Button(root,
										text="Click Me!",
										command=say_hello)
	button.pack()

	label = tk.Label(root,
									text="Hallo User")
	label.pack()

	root.mainloop()