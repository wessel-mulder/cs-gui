import tkinter as tk
from tkinter import filedialog

import tkinter as tk
from tkinter import filedialog

def Browse_xlsx(self, button_name, question, label_update, callback, initial_dir='/'):
    def browseXlsx():
        filetypes = [("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        file_selected = filedialog.askopenfilename(initialdir=initial_dir, title="Select an Excel File", filetypes=filetypes)
        
        if file_selected:
            label_file_explorer.configure(text=label_update + file_selected)
            callback(file_selected)

    # Create a File Explorer label
    label_file_explorer = tk.Label(self, text=question, height=2,wraplength = 500)
    button_explore = tk.Button(self, text=button_name, borderwidth=2, relief="solid", command=browseXlsx,wraplength=500)
    
    label_file_explorer.pack()
    button_explore.pack()

def Browse_folder(self, button_name, question, label_update, callback, initial_dir='/'):
    def browseFolders():
        folder_selected = filedialog.askdirectory(initialdir=initial_dir, title="Select a Folder")

        if folder_selected:
            label_file_explorer.configure(text=label_update + folder_selected)
            callback(folder_selected)

    # Create a File Explorer label
    label_file_explorer = tk.Label(self, text=question, height=2,wraplength=500)
    button_explore = tk.Button(self, text=button_name,borderwidth=2, relief="solid", command=browseFolders,wraplength=500)
    
    label_file_explorer.pack()
    button_explore.pack()

def Browse_txt(self, button_name, question, label_update, callback, initial_dir='/'):
    def browseTexts():
        filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
        file_selected = filedialog.askopenfilename(initialdir=initial_dir, title="Select a .txt file", filetypes=filetypes)
        
        if file_selected:
            label_file_explorer.configure(text=label_update + file_selected)
            callback(file_selected)

    # Create a File Explorer label
    label_file_explorer = tk.Label(self, text=question, height=2,wraplength=500)
    button_explore = tk.Button(self, text=button_name,borderwidth=2, relief="solid", command=browseTexts,wraplength=500)
    
    label_file_explorer.pack()
    button_explore.pack()


#Name of the last checked excel sheet from the KOBO website ('empty' for first check) (TO BE CHANGED)
previous = 'empty' 

#Name of the newly downloaded excel sheet from the KOBO website (TO BE CHANGED)
current = 'CS_unchecked_1505_test.xlsx'

#Name of the new excel file to save too (= 'current_Temp') (TO BE CHANGED)
temp = 'CS_checked_1505_test.xlsx'

# Name of the csv-file containing the true coordinates of all the sites (not to be changed)
# Changes to column names in this file need to be adjusted below! Also adding the correct Village names might be required.
# The spelling of the Village names must be as in the KOBO Data.
coordinates = 'coordinates.xlsx'




