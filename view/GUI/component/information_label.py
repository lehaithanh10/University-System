import tkinter as tk


def information_label(master, title: str):
    return tk.Label(master, text=title, font="Helvetica 16 bold", pady=10).pack()
