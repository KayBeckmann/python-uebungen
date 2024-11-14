import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

def close():
    if quitProgramm.get():
        quit()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("150x80")

    quitProgramm = tk.BooleanVar()

    checkButton = ctk.CTkCheckBox(root,
                                 text = "Beenden?",
                                 font = ("Arial", 10),
                                 variable = quitProgramm)
    checkButton.pack()

    ctk.CTkButton(root,
              text = "Schließen",
              command = close ).pack()
    
    root.mainloop()