import tkinter as tk

def close():
    if quitProgramm.get():
        quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("150x80")

    quitProgramm = tk.BooleanVar()

    checkButton = tk.Checkbutton(root,
                                 text = "Beenden?",
                                 font = ("Arial", 10),
                                 variable = quitProgramm)
    checkButton.pack()

    tk.Button(root,
              text = "Schließen",
              command = close ).pack()
    
    root.mainloop()