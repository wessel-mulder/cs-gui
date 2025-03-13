from tkinter import filedialog, messagebox
from tkinter import *
import pandas as pd


def read_from_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Introduction file not found."
    

def create_excel_sheet(self):
    # Get the input from the entry widget
    sheet_name = self.sheet_name_entry.get()
    
    if not sheet_name:
        messagebox.showwarning("Input Error", "Sheet name cannot be empty!")
        return
    
    # Create a new Excel file with the specified sheet name
    try:
        # Create a DataFrame as an example
        df = pd.DataFrame({"Data": [1, 2, 3, 4, 5]})
        
        # Save the DataFrame to an Excel file with the specified sheet name
        file_path = "new_excel_file.xlsx"
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        messagebox.showinfo("Success", f"Excel sheet '{sheet_name}' created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")