import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime

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

# reading in existing file
# if file does not exist or can't be found, a new one wil be created in safeClicked()
try:
    file = (r'C:\Users\david\OneDrive\Dokumenter\GitHub\Friends.xlsx')
    existing_df = pd.read_excel(file, sheet_name=0, index_col=0)
    # evaluating the highes entry count
    db_id_nu = existing_df['DB ID'].max() + 1
except:
    fileNotExistant = True

# entry field refreshable
def entryFrameFunction():
    global addFirstTimeClicked
    global db_idString
    global entryOK

    # find entry button clicked
    def findClicked():

        # define correction field
        def correctionFunction():
            
            itemToChange = tk.StringVar()
            entryToCorrect = tk.IntVar()

            # return button clicked
            def returnClicked():
                correctionFrame.destroy()
                entryFrameFunction()

            # correct button clicked
            def correctClicked():
                global dontDestroy
                global db_entryTimeStamp

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
                saveClicked()
            
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
                entryFrameFunction()

            # check if age is in allowed range 0 - 100
            # saving variables into dictionarys if in range
            if ageInt < 0 or ageInt > 100:
                entryOK = False
                entryFrame.destroy()
                entryFrameFunction()

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
                entryFrameFunction()

        # else display message to enter all fields
        else:
            headline_label["text"] = "Please fill in all fields!"
    
    # save button clicked
    def saveClicked():
        global dontDestroy
        global db_entryTimeStamp

        f = {"DB ID" : db_id, "first name" : db_fname, "last name" : db_lname, "age" : db_age, "entry time stamp" : db_entryTimeStamp}
        new_df = pd.DataFrame(f, index=db_id)

        if fileNotExistant == True:
            new_df.to_excel('Friends.xlsx')
            root.destroy()
            print(new_df)
        else:
            df = pd.concat([existing_df, new_df])
            df.to_excel('Friends.xlsx')
            print(df)

            if dontDestroy == False:
                root.destroy()
                os.startfile(r'C:\Users\david\OneDrive\Dokumenter\GitHub\creatingDatabaseViaEntryField\plotStat.py')
            else:
                dontDestroy = False
                entryFrameFunction()

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
       save_button = ttk.Button(entryFrame, text="Save entry number " + db_idString + " to Friends.xlsx?", command=saveClicked)
       save_button.pack(fill='y', expand=True, pady=10) 
    
    # correct entry button
    find_button = ttk.Button(entryFrame, text="Find entry", command=findClicked)
    find_button.pack(fill='y', expand=True, pady=10)

# root window
root = tk.Tk()
root.geometry("330x300")
root.resizable(True, True)
root.title('Database Entry')

entryFrameFunction()

root.mainloop()