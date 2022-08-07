import matplotlib.pyplot as plt
import pandas as pd

lastNames = []
lastNamesCount = []

# importing dataframe from execl sheet.
try:
    file = (r'C:\Users\david\OneDrive\Dokumenter\GitHub\Friends.xlsx')
    df = pd.read_excel(file, sheet_name=0, index_col=0)
# except to prevent freezing
except:
    print("File can't be found, please check if file at correct location!")

# filtering the surnames
stat_lname = df.loc[: , 'last name']
stat_lname = stat_lname.value_counts()

# transfering stat in tuples
for index, value in stat_lname.items():
    lastNames.append(index)
    lastNamesCount.append(value)

# plotting a bar chart
plt.bar(lastNames, lastNamesCount, tick_label = lastNames,
        width = 0.4, color = ['blue', 'black'],)
  
# naming x-, y-axis and title
plt.xlabel('Last names')
plt.ylabel('Occurencies')
plt.title('Occurencies of last names in database')

# display the plot
plt.show()