import pandas as pd
import tkinter as tk
from tkinter import ttk

db_fname = {}
db_lname = {}
db_age = {}
db_entry = {}
entryNumber = 0
addFirstTimeClicked = False
entryNumberString = "0"
entryOK = True

# entry field refreshable
def entryFrameFunction():
    global addFirstTimeClicked
    global entryNumberString
    global entryOK

    # add button clicked
    def addClicked():
        global addFirstTimeClicked
        global entryNumber
        global entryNumberString
        global entryOK
        ageInt = 0

        # check if all fields are filled
        inputFilter = ""
        if fname.get() != inputFilter and lname.get() != inputFilter and age.get() != inputFilter:
            
            # check if age is a integer
            try:
                ageInt = int(age.get())
                entryOK = True

                # saving variables into dictionarys
                db_entry[entryNumber] = entryNumber + 1
                db_fname[entryNumber] = fname.get()
                db_lname[entryNumber] = lname.get()
                db_age[entryNumber] = ageInt
                addFirstTimeClicked = True
                entryNumber = entryNumber + 1
                entryNumberString = str(entryNumber)
                entryOK = True
                entryFrame.destroy()
                entryFrameFunction()

            except:
                entryOK = False
                entryFrame.destroy()
                entryFrameFunction()

        # else display message to enter all fields
        else:
            headline_label["text"] = "Please fill in all fields!"
    
    # save button clicked
    def saveClicked():
        f = {"entry" : db_entry, "first name" : db_fname, "last name " : db_lname, "age" : db_age}
        df = pd.DataFrame(f)
        df.to_excel('Friends.xlsx')
        root.destroy()

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
        headline_label = ttk.Label(entryFrame, text="Age must be a number, try again dumb!")
        headline_label.pack(fill='y', expand=True)

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
       save_button = ttk.Button(entryFrame, text="Save " + entryNumberString + " entry to Excel?", command=saveClicked)
       save_button.pack(fill='y', expand=True, pady=10) 

# root window
root = tk.Tk()
root.geometry("330x300")
root.resizable(True, True)
root.title('Database Entry')

entryFrameFunction()

root.mainloop()