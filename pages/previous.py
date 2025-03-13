import tkinter as tk

class PreviousPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Reference to the main application
        self.lang_dict = controller.lang_dict
        self.language = controller.language

        self.label_wd = tk.Label(self, text=self.lang_dict['previous']['wd'][self.language])
        self.label_wd.pack()
        self.label_image = tk.Label(self, text=self.lang_dict['previous']['image'][self.language])
        self.label_image.pack()
        self.label_kobo = tk.Label(self, text=self.lang_dict['previous']['kobo'][self.language])
        self.label_kobo.pack()
        self.label_coordinates = tk.Label(self, text=self.lang_dict['previous']['coordinates'][self.language])
        self.label_coordinates.pack()
        self.label_previous = tk.Label(self, text=self.lang_dict['previous']['previous'][self.language])
        self.label_previous.pack()
        self.label_new = tk.Label(self, text=self.lang_dict['previous']['new'][self.language])
        self.label_new.pack()
        self.label_settings = tk.Label(self, text=self.lang_dict['previous']['settings'][self.language])
        self.label_settings.pack()
        
        # Button to go to start validating
        self.validate_button = tk.Button(self, text=self.lang_dict['previous']['validate_button'][self.language],
                                      command=lambda: controller.show_frame("ValidationPage"))
        self.validate_button.pack()

        # Button to go to the Data Description page
        self.back_data_button = tk.Button(self, text=self.lang_dict['previous']['back_data_button'][self.language],
                                      command=lambda: controller.show_frame("DataDescriptionPage"))
        self.back_data_button.pack()

        self.back_start_button = tk.Button(self, text=self.lang_dict['previous']['back_start_button'][self.language],
                                     command=lambda: controller.show_frame("StartPage"))
        self.back_start_button.pack(pady=20)
        
    def update_labels(self, wd, image, kobo, coordinates, previous, new,settings):
        self.label_wd.config(text=f"{self.lang_dict['previous']['wd'][self.language]}{wd}")
        self.label_image.config(text=f"{self.lang_dict['previous']['image'][self.language]}{image}")
        self.label_kobo.config(text=f"{self.lang_dict['previous']['kobo'][self.language]}{kobo}")
        self.label_coordinates.config(text=f"{self.lang_dict['previous']['coordinates'][self.language]}{coordinates}")
        self.label_previous.config(text=f"{self.lang_dict['previous']['previous'][self.language]}{previous}")
        self.label_new.config(text=f"{self.lang_dict['previous']['new'][self.language]}{new}")
        self.label_settings.config(text=f"{self.lang_dict['previous']['settings'][self.language]}{settings}")


    def update_values(self, wd, image, kobo, coordinates, previous, new, settings):
        self.wd = wd
        self.image = image
        self.kobo = kobo
        self.coordinates = coordinates
        self.previous = previous
        self.new = new
        self.settings = settings

    def get_language(self):
        return self.language
    
    def get_lang_dict(self):
        return self.lang_dict

    def update_values_langdict(self, lang, dict):
        self.language = lang
        self.lang_dict = dict
