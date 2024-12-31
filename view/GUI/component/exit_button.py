import tkinter as tk


def exit_button(master, title, click_function):
    return tk.Button(
        master,
        text=title,
        bg="red",
        fg="white",
        font="Helvetica 14",
        command=click_function,
        height=2,
    ).pack()
