import tkinter as tk

from view.GUI.screen.main_menu_system_screen import main_menu_system_screen

root = tk.Tk()
root.title("University System Menu")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
main_menu_system_screen(root)
root.mainloop()
