import tkinter as tk

def Header(self, input):
    self.label = tk.Label(self, text=input, font=('Arial', 18))
    self.label.pack()

def Main(self, input, color = None):
    self.intro_message = tk.Message(self, text=input, width=700, font=('Arial', 12), fg = color)
    self.intro_message.pack()