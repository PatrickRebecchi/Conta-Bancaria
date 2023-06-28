from interface import Interface
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)
    interface.iniciar()
    root.mainloop()
