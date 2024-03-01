import pandas as pd
import numpy as np

col = input("Enter column you want: ")  # Enter column name, 
# This app will get that column and write it to a text file
numbers = pd.read_excel('in.xlsx', usecols=col)
file = open("out.txt", "w")
for index, row in numbers.iterrows():
    if not np.isnan(row[col]):
        file.write(f"0{int(row[col])}\n")
        
file.close()