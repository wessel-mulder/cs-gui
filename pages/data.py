import tkinter as tk
from aesthetics.text import Header
from aesthetics.buttons import Browse_folder, Browse_xlsx, Browse_txt
import datetime

class DataDescriptionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # Initialize the Frame class with parent
        self.controller = controller  # Reference to the main application
        self.lang_dict = controller.lang_dict
        self.language = controller.language

        Header(self, self.lang_dict['data']['welcome'][self.language])

        # Introduction text
        # Get current date

        self.wd = Browse_folder(self,
                                self.lang_dict['data']['browse_wd'][self.language],
                                self.lang_dict['data']['select_wd'][self.language],
                                self.lang_dict['data']['confirm_wd'][self.language],
                                self.set_wd)
        #self.wd = '/Volumes/T7/CS_job/CS_gui'
        #self.wd = 'E:\CS_job\CS_gui'

        self.image = Browse_folder(self,
                                self.lang_dict['data']['browse_image'][self.language],
                                self.lang_dict['data']['select_image'][self.language],
                                self.lang_dict['data']['confirm_image'][self.language],
                                self.set_image)
        #self.image = '/Volumes/T7/CS_job/CS_gui/images/'
        #self.image = 'E:\CS_job\CS_gui\images'

        self.kobo = Browse_xlsx(self,
                                self.lang_dict['data']['browse_kobo'][self.language],
                                self.lang_dict['data']['select_kobo'][self.language],
                                self.lang_dict['data']['confirm_kobo'][self.language],
                                self.set_kobo)
        #self.kobo = '/Volumes/T7/CS_job/CS_gui/CS_unchecked_1505_test.xlsx'
        #self.kobo = 'E:\CS_job\CS_gui\CS_unchecked_1505_test.xlsx'


        self.coordinates = Browse_xlsx(self,
                                self.lang_dict['data']['browse_coordinates'][self.language],
                                self.lang_dict['data']['select_coordinates'][self.language],
                                self.lang_dict['data']['confirm_coordinates'][self.language],
                                self.set_coordinates)
        #self.coordinates = '/Volumes/T7/CS_job/CS_gui/coordinates.xlsx'
        #self.coordinates = 'E:\CS_job\CS_gui\coordinates.xlsx'


        self.previous = 'None'
        self.previous = Browse_xlsx(self,
                                self.lang_dict['data']['browse_previous'][self.language],
                                self.lang_dict['data']['select_previous'][self.language],
                                self.lang_dict['data']['confirm_previous'][self.language],
                                self.set_previous)
        
        self.settings = Browse_txt(self,
                                self.lang_dict['data']['browse_settings'][self.language],
                                self.lang_dict['data']['select_settings'][self.language],
                                self.lang_dict['data']['confirm_settings'][self.language],
                                self.set_settings)
        #self.settings = '/Volumes/T7/CS_job/CS_gui/settings.txt'
        #self.settings = 'E:\CS_job\CS_gui\settings.txt'


        tk.Label(self, text="Enter your name:").pack(pady=10)

        name_entry = tk.Entry(self)
        name_entry.pack(pady=5)

        self.name_entry = name_entry
        controller.name_entry = name_entry  
        
        current_date = datetime.datetime.now()
        # Format date as year_month_day
        formatted_date = current_date.strftime("%Y%m%d_%H%M")      # get date
        self.new = 'CS_validation_' + formatted_date + '.xlsx'

        self.date_current = current_date.strftime("%Y-%m-%d")
        # Button to go to the Data Description page
        self.start_button = tk.Button(self, text=self.lang_dict['data']['next_page'][self.language],
                                      command=lambda: controller.show_frame("PreviousPage"))
        self.start_button.pack()

        self.back_button = tk.Button(self, text=self.lang_dict['data']['back_button'][self.language],
                                     command=lambda: controller.show_frame("StartPage"))
        self.back_button.pack(pady=20)

    def set_wd(self, path):
        self.wd = path

    def set_image(self, path):
        self.image = path

    def set_kobo(self, path):
        self.kobo = path

    def set_coordinates(self, path):
        self.coordinates = path

    def set_previous(self, path):
        self.previous = path

    def set_new(self, path):
        self.new = path
    
    def set_settings(self, path):
        self.settings = path

    def get_wd(self):
        return self.wd

    def get_image(self):
        return self.image

    def get_kobo(self):
        return self.kobo

    def get_coordinates(self):
        return self.coordinates

    def get_previous(self):
        return self.previous

    def get_new(self):
        return self.new
    
    def get_language(self):
        return self.language
    
    def get_lang_dict(self):
        return self.lang_dict
    
    def get_name(self):
        return self.name_entry

    def get_date(self):
        return self.date_current

    def get_settings(self):
        return self.settings

    def update_values_langdict(self, lang, dict):
        self.language = lang
        self.lang_dict = dict
