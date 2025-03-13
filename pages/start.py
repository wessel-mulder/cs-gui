import tkinter as tk
from sides import read_from_txt
from aesthetics.text import Header,Main



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # Initialize the Frame class with parent
        self.controller = controller  # Reference to the main application
        self.lang_dict = controller.lang_dict
        self.language = controller.language




        Header(self,self.lang_dict['start']['welcome'][self.language])

        # Introduction text
        #intro_text = read_from_txt("introduction.txt")
        Main(self,self.lang_dict['start']['intro_text'][self.language])


        # Button to go to the Data Description page
        self.start_button = tk.Button(self, text=self.lang_dict['start']['start_button'][self.language],
                                      command=lambda: self.controller.show_frame('DataDescriptionPage'))
        self.start_button.pack()

    def choose_english(self):
        self.language = 'en'
        self.english_button.config(foreground='blue')
        self.french_button.config(foreground='black')

    def choose_french(self):
        self.language = 'fr'
        self.french_button.config(foreground='blue')
        self.english_button.config(foreground='black')
    
    def update_all_frames(self):
        self.controller.update_all_frames(self.language)

    def start_application(self):
        self.controller.create_pages()
        self.controller.show_frame("DataDescriptionPage")

    def get_language(self):
        return self.language

    def get_lang_dict(self):
        return self.lang_dict
