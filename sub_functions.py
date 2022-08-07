import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# all functions related 


# correct button clicked
def correctClicked(dontDestroy):

    db_entryTimeStamp = datetime.now()

    # updating choosen entry and item
    # checking if age then converting to integer
    if dropdown.get() == 'age':
        itemToChangeX = int(itemToChange.get())

    elif dropdown.get() == 'delete':
        existing_df.drop([entryToCorrect.get()], inplace=True)
                    
    else:
        itemToChangeX = itemToChange.get()
        existing_df.loc[[entryToCorrect.get()], [dropdown.get()]] = itemToChangeX

        dontDestroy = True
        correctionFrame.destroy()
        my_functions.saveClicked(dontDestroy, db_entryTimeStamp)

# return button clicked
def returnClicked():
    correctionFrame.destroy()
    entryFrame()

# define correction field
def correctionFunction():
            
    itemToChange = tk.StringVar()
    entryToCorrect = tk.IntVar()

    # correction frame
    correctionFrame = ttk.Frame(root)
    correctionFrame.pack(padx=10, pady=10, fill='x', expand=True)

    # label for found first name if not 0
    if fname_search != '0':
        found_fname_label = ttk.Label(correctionFrame, text= fname_search)
        found_fname_label.pack(fill='x', expand=False)

    # label for found last name if not 0
    if lname_search != '0':
        found_lname_label = ttk.Label(correctionFrame, text= lname_search)
        found_lname_label.pack(fill='x', expand=True)

    # label for entry
    db_id_label = ttk.Label(correctionFrame, text="Entry number to be corrected: ")
    db_id_label.pack(fill='y', expand=True)

    # field for correcting specific entry number
    db_id_entry = ttk.Entry(correctionFrame, textvariable=entryToCorrect)
    db_id_entry.pack(fill='y', expand=True)
    db_id_entry.focus()

    # label for dropdown
    dropdown_label  = ttk.Label(correctionFrame, text="Choose which item shall be updated: ")
    dropdown_label.pack(fill='y', expand=True)

    # dropdown for correcting specific detail
    dropdown = ttk.Combobox(correctionFrame, values=["first name", "last name", "age", "delete"])
    dropdown.pack(fill='y', expand=True)

    # label for item change
    changeItem_label  = ttk.Label(correctionFrame, text="Enter item update: ")
    changeItem_label.pack(fill='y', expand=True)

    # entry for correcting in dropdown choosen item
    changeItem_entry = ttk.Entry(correctionFrame, textvariable=itemToChange)
    changeItem_entry.pack(fill='y', expand=True)
    changeItem_entry.focus()

    # button for correcting entry
    correct_button = ttk.Button(correctionFrame, text="Correct entry?", command=correctClicked)
    correct_button.pack(fill='y', expand=True, pady=10)

    # return button to star field
    return_button = ttk.Button(correctionFrame, text="Return to start", command=returnClicked)
    return_button.pack(fill='y', expand=True, pady=10)

def gotoStat():
    global dontDestroy
    global db_entryTimeStamp

    dontDestroy = False
    db_entryTimeStamp = datetime.now()
    my_functions.saveClicked(dontDestroy)

# add button clicked
def addClicked():
    global addFirstTimeClicked
    global db_id_nu
    global db_idString
    global entryOK
    global db_entryTimeStamp
    ageInt = 0

    # check if all fields are filled
    inputFilter = ""
    if fname.get() != inputFilter and lname.get() != inputFilter and age.get() != inputFilter:
            
        # check if age is a integer
        try:
            ageInt = int(age.get())
            entryOK = True

        except:
            entryOK = False
            entryFrame.destroy()
            entryFrame()

        # check if age is in allowed range 0 - 100
        # saving variables into dictionarys if in range
        if ageInt < 0 or ageInt > 100:
            entryOK = False
            entryFrame.destroy()
            entryFrame()

        else:
            db_id.append(db_id_nu)
            db_fname[db_id_nu] = fname.get()
            db_lname[db_id_nu] = lname.get()
            db_age[db_id_nu] = ageInt
            db_entryTimeStamp = datetime.now()
            print(db_entryTimeStamp)
            addFirstTimeClicked = True
            db_id_nu = db_id_nu + 1
            db_idString = str(db_id_nu)
            entryOK = True
            entryFrame.destroy()
            entryFrame()

    # else display message to enter all fields
    else:
        headline_label["text"] = "Please fill in all fields!"

# find entry button clicked
def findClicked():

    # searching for entryed first name in excel file
    try:
        fname_search = existing_df.loc[existing_df["first name"] == fname.get()]
            
        # testing if df is empty
        if fname_search.empty:
            fname_search = '0'
        else:
            fname_search = fname_search.to_string()

    except:
        fname_search = '0'

    try:
        lname_search = existing_df.loc[existing_df["last name"] == lname.get()]

        # testing if df is empty
        if lname_search.empty:
            lname_search = '0'
        else:
            lname_search = lname_search.to_string()

    except:
        lname_search = '0'

    # search all function
    if fname.get() == 'all':
        fname_search = existing_df.to_string()

    # determinating if fname and lname are the same result, deleting lname if the same
    if fname_search == lname_search:
        lname_search = '0'

    # chanigng the displayed field
    entryFrame.destroy()
    correctionFunction()