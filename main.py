import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sub_functions

db_fname = {}
db_lname = {}
db_age = {}
db_id = []
db_id_nu = 0
df = {}
addFirstTimeClicked = False
db_idString = "0"
entryOK = True
fileNotExistant = False
dontDestroy = False

# entry field refreshable
def entryFrame():
    global addFirstTimeClicked
    global db_idString
    global entryOK


    # store variables
    fname = tk.StringVar()
    lname = tk.StringVar()
    age = tk.StringVar()

    # entry frame
    entryFrame = ttk.Frame(root)
    entryFrame.pack(padx=10, pady=10, fill='y', expand=True)

    # header label
    if entryOK == True:
        headline_label = ttk.Label(entryFrame, text="Please enter details to be added to database: Friends.xlsx")
        headline_label.pack(fill='y', expand=True)

    else:
        headline_label = ttk.Label(entryFrame, text="Age must be a number between 0 and 100, try again dumb!")
        headline_label.pack(fill='y', expand=True)
        entryOK = True

    # first name label + entry field
    fname_label = ttk.Label(entryFrame, text="Enter first name: ")
    fname_label.pack(fill='y', expand=True)

    fname_entry = ttk.Entry(entryFrame, textvariable=fname)
    fname_entry.pack(fill='x', expand=True)
    fname_entry.focus()

    # last name label + entry field
    lname_label = ttk.Label(entryFrame, text="Enter last name: ")
    lname_label.pack(fill='y', expand=True)

    lname_entry = ttk.Entry(entryFrame, textvariable=lname)
    lname_entry.pack(fill='x', expand=True)
    lname_entry.focus()

    # age name label + entry field
    age_label = ttk.Label(entryFrame, text="Enter the age: ")
    age_label.pack(fill='y', expand=True)

    age_entry = ttk.Entry(entryFrame, textvariable=age)
    age_entry.pack(fill='x', expand=True)
    age_entry.focus()

    # add button
    add_button = ttk.Button(entryFrame, text="Add", command=addClicked)
    add_button.pack(fill='y', expand=True, pady=10)

    # save button
    if addFirstTimeClicked == True:
       save_button = ttk.Button(entryFrame, text="Save entry number " + db_idString + " to Friends.xlsx?", command=my_functions.saveClicked(dontDestroy))
       save_button.pack(fill='y', expand=True, pady=10) 
    
    # correct entry button
    find_button = ttk.Button(entryFrame, text="Find entry", command=findClicked)
    find_button.pack(fill='y', expand=True, pady=10)

    # goto statistic button
    stat_button = ttk.Button(entryFrame, text="Go to statistic (will save changes)", command=gotoStat)
    stat_button.pack(fill='y', expand=True, pady=10)

# root window
root = tk.Tk()
root.geometry("330x300")
root.resizable(True, True)
root.title('Database Entry')

# reading in existing EXCEL file
# if file does not exist or can't be found, a new one wil be created in safeClicked()
try:
    file = (r'C:\Users\david\OneDrive\Dokumenter\GitHub\Friends.xlsx')
    existing_df = pd.read_excel(file, sheet_name=0, index_col=0)
    # evaluating the highes entry count
    db_id_nu = existing_df['DB ID'].max() + 1
except:
    fileNotExistant = True

entryFrame()



root.mainloop()