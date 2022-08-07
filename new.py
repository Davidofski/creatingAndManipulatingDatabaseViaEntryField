import random
import tkinter as tk
from tkinter import ttk
import datetime as dt

def refresh(*args):

    y = dt.datetime.now()
    z = str(y)
    print(y)
    x = random.randint(2, 10000)
    string = ('Nacho loves climbing {0:0.0f} times more than David at ' + z).format(x)
    ground_timer_label['text'] = string


# string to begin with
string = 'How many times does Nacho like to climbe more than David?'

# root window
root = tk.Tk()
root.geometry("450x200")
root.resizable(False, False)
root.title('Database Entry')

# frame to name timer
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='y', expand=True)

# ground timer label + entry
ground_timer_label = ttk.Label(signin, text=string)
ground_timer_label.pack(fill='y', expand=True)


# gues button
start_button = ttk.Button(signin, text="Start", command=refresh(5))
start_button.pack(fill='y', expand=False, pady=10)

root.mainloop()