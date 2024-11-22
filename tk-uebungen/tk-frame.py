import tkinter as tk

def button1():
    print("ONE")

def button2():
    print("TWO")

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Frames")
    root.geometry("250x100")

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame,
              text="Button 1",
              command=button1).pack()
    
    tk.Button(button_frame,
              text="Button 2",
              command=button2).pack()
    
    root.mainloop()