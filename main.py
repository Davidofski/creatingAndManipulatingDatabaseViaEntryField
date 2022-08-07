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


root.mainl oop()