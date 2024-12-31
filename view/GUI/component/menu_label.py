import tkinter as tk


def menu_label(master, title: str):
    return tk.Label(
        master, text=title, padx=20, pady=20, font="Helvetica 16 bold"
    ).pack()
