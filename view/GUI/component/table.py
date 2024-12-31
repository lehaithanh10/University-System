import tkinter as tk


def table(master, data, headers, row_existing):
    print_data = headers + [list(element.values()) for element in data]

    for i in range(len(print_data)):
        for j in range(len(print_data[0])):
            width = 15
            if j == 1:
                width = 20
            if j == 2:
                width = 35

            e = tk.Entry(master, width=width, fg="blue",
                         font=("Arial", 12, "bold"))
            e.grid(row=i + row_existing, column=j + 1)
            e.insert(tk.END, print_data[i][j])
