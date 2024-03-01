import pandas as pd
from typing import List

def save(filename: str, numbers: List[str]):
    dot_index = 1
    while dot_index <= len(filename) and filename[-dot_index] != '.':
        dot_index += 1
    if dot_index < len(filename):
        filename  = filename[:-dot_index] + ".txt"
    file = open(filename, "w")
    file.write('\n'.join(numbers))
    file.close()
    
        
def read_excel_columns(file_path: str) -> bool:
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        numbers = []
        # Iterate through each column
        for row in df.columns:
            columns = df[row].tolist()

            for cell in columns:
                try:
                    if cell in numbers:  # prevent repetitive numbers
                        continue
                    int(cell)
                    # if its a number:
                    ln = len(cell)
                    if (cell[0] == '0' and ln == 11) or (cell[0] == '+' and ln >= 12 and ln <= 14):
                        numbers.append(cell)
                except:
                    pass
        save(file_path, numbers)
    except Exception as e:
        print(f"Error reading Excel file called {file_path}: {e}")
        return False
    return True


if __name__ == "__main__":
    file_paths =  ('file1.xlsx', 'file2.xlsx', 'whatever...xlsx') # put any number of excel files here, 
    # this app will read them, extract phone numbers and save it in a text file with the same name
    for file_path in file_paths:
        if read_excel_columns(file_path):
            print(f"{file_path} saved successfully.")
        else:
            print(f"Couldn't read numbers from {file_path}.")
