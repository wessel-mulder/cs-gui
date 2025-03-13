import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from os import path
import pandas as pd

class CorrectionWindow(tk.Toplevel):
    def __init__(self, parent, row, folder, pics, index, df):
        super().__init__(parent)
        self.row = row
        self.folder = folder
        self.pics = pics
        self.index = index
        self.df = df

        self.title(f"Correction for ID {row['ID']}")
        self.geometry("800x600")

        self.display_image('Placez tous les escargots vivants dans le carré marqué sur le papier milimètré et prenez une photo.')

    def display_image(self, column_name):
        image_name = str(self.row[column_name])
        image_path = path.join(self.folder, self.pics, self.row['_uuid'], image_name)

        if path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((400, 400), Image.ANTIALIAS)  # Resize the image
            photo = ImageTk.PhotoImage(image)
            
            # Create a label to display the image
            label = tk.Label(self, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(pady=10)
        else:
            messagebox.showerror("Error", f"Image not found: {image_path}")

if __name__ == "__main__":
    # Example usage in a standalone script
    folder = '/Volumes/T7/CS_job/CS_validation/start1605/'
    pics = 'images/'
    current = 'CS_checked_1505.xlsx'
    temp = 'CS_corrected_1505.xlsx'

    # Example dataframe initialization (replace with your actual data loading logic)
    df = pd.read_excel(path.join(folder, current))

    # Example row selection (replace with your logic to iterate over rows)
    index = 0
    row = df.iloc[index]

    # Initialize the correction window
    root = tk.Tk()
    window = CorrectionWindow(root, row, folder, pics, index, df)
    root.mainloop()