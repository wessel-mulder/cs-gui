import tkinter as tk
from tkinter import ttk
from aesthetics.text import Main
from pages.checking import start_check, print_erros, destroy_this_button
from tkscrollableframe import ScrolledFrame, ScrollbarsType

import numpy as np
import pandas as pd
from datetime import datetime
import os.path

class ValidationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.language = controller.language
        self.lang_dict = controller.lang_dict
        self.name_entry = controller.name_entry
        self.update_idletasks()

        #self.wd = None
        #self.image = None
        #self.kobo = None
        #self.coordinates = None
        #self.previous = None
        #self.new = None

        # Create and pack widgets here (if any)

        # Button to go back to Data Description Page
        #self.back_button = tk.Button(self, text="Back to Data Description Page",
       #                             command=lambda: controller.show_frame("DataDescriptionPage"))
       # self.back_button.pack(pady=20)

        # Button to go to the next page
      #  self.next_button = tk.Button(self, text="Go to the Previous Page",
      #                               command=lambda: controller.show_frame("PreviousPage"))
       # self.next_button.pack(pady=20)
                   # Read Kobo data

        # Button to open a new window

        self.counter = 0
        self.new_window_button = tk.Button(self, text=self.lang_dict['validation']['start_validation'][self.language], command=self.open_new_window, borderwidth=2, relief="solid")
        self.new_window_button.pack(pady=10)

        self.back_data_button = tk.Button(self, text=self.lang_dict['previous']['back_data_button'][self.language],
                                      command=lambda: controller.show_frame("DataDescriptionPage"))
        self.back_data_button.pack()

#### PRE PROCESSING DATA
    def update_values(self, wd, image, kobo, coordinates, previous, new, name, date,settings):
        self.wd = wd
        self.image = image
        self.kobo = kobo
        self.coordinates = coordinates
        self.previous = previous
        self.new = new
        self.name_entry = name
        self.date_current = date
        self.settings = settings
    
    def process_data(self):
        self.df = pd.read_excel(self.kobo)

        self.coordinates_df = pd.read_excel(self.coordinates)
        self.villages = set(self.coordinates_df["Name village"])
        self.Lat = np.mean(self.coordinates_df["Fixed site Latitude "]) # in decimal degrees

        with open(self.settings, 'rb') as file:
            settings = eval(file.read())
        
        self.empty_bio_q = settings['empty_bio_q']
        self.empty_bio_img = settings['empty_bio_img']
        self.empty_bul_q = settings['empty_bul_q']
        self.empty_bul_img = settings['empty_bul_img']
        self.empty_lym_q = settings['empty_lym_q']
        self.empty_lym_img = settings['empty_lym_img']
        self.empty_pool_q = settings['empty_pool_q']
        self.empty_pool_img = settings['empty_pool_img']

        self.live_bio_q = settings['live_bio_q']
        self.live_bio_img = settings['live_bio_img']
        self.live_bul_q = settings['live_bul_q']
        self.live_bul_img = settings['live_bul_img']
        self.live_lym_q = settings['live_lym_q']
        self.live_lym_img = settings['live_lym_img']
        self.live_pool_q = settings['live_pool_q']
        self.live_pool_img = settings['live_pool_img']

        self.img_living = settings['img_living']
        self.img_empty = settings['img_empty']

        self.village_col = settings['village_col']
        self.date_col = settings['date_col']
        self.longitude_col = settings['longitude_col']
        self.latitude_col = settings['latitude_col']
        self.start_sampling = settings['start_sampling']
        self.end_sampling = settings['end_sampling']

        self.any_snails_found = settings['any_snails_found']
        self.any_found_no = settings['any_found_no']
        self.any_found_yes = settings['any_found_yes']
        self.which_snails_found = settings['which_snails_found']
        self.just_live = settings['just_live']
        self.just_empty = settings['just_empty']

        self.tmin = pd.to_timedelta(settings['min_scooptime']) # minimum time to scoop
        self.tmax = pd.to_timedelta(settings['max_scooptime']) # maximum time to scoop

        self.start_date = datetime(settings['date_min'][0],settings['date_min'][1],settings['date_min'][2]).date()
        self.end_date = datetime(settings['date_max'][0],settings['date_max'][1],settings['date_max'][2]).date()

        self.Dmax = settings['max_distance'] # in meters
        self.Dmax_x = self.Dmax / (111320 * np.cos(np.radians(self.Lat))) # converts to decimal degrees
        self.Dmax_y = self.Dmax / 111320

        if '_validation_status' not in self.df.columns:
            self.df['_validation_status'] = 0
            self.df['ID_Error'] = 0
            self.df['Date_warning'] = 0
            self.df['Location_Error'] = 0
            self.df['Distance_Error'] = 0            
            self.df['Scoop_Time_Error'] = 0
            self.df['Images_Missing'] = 0
            self.df['Bio_Live_Image_Missing'] = 0
            self.df['Bul_Live_Image_Missing'] = 0
            self.df['Lym_Live_Image_Missing'] = 0
            self.df['Pool_Live_Image_Missing'] = 0
            self.df['Bio_Empty_Image_Missing'] = 0
            self.df['Bul_Empty_Image_Missing'] = 0
            self.df['Lym_Empty_Image_Missing'] = 0
            self.df['Pool_Empty_Image_Missing'] = 0
            self.df['Shells_Error'] = 0
            self.df['Counting_Error'] = 0
            self.df['Identification_Error'] = 0 
            self.df['Bio_Error'] = 0
            self.df['Bul_Error'] = 0
            self.df['Lym_Error'] = 0
            self.df['Pool_Error'] = 0
            self.df['Bio_live_corrected']=0
            self.df['Bul_live_corrected']=0
            self.df['Lym_live_corrected']=0
            self.df['Pool_live_corrected'] = 0
            self.df['Bio_empty_corrected']=0
            self.df['Bul_empty_corrected']=0
            self.df['Lym_empty_corrected']=0
            self.df['Pool_empty_corrected']=0
            self.df['Validation_by']=0
            self.df['Validation_date'] = 0

        if self.previous is None:
            self.df_prev = pd.DataFrame(self.df[0:0].copy())
            self.df_prev.to_excel(os.path.join(self.wd,self.new))
        else:
            self.df_prev = pd.read_excel(self.previous)

        self.num_rows = self.df.shape[0]

        self.indexes = self.get_indexes_not_validated()

    def get_indexes_not_validated(self):
            indexes_not_validated = self.df[self.df['_validation_status'] != 1].index.tolist()
            return indexes_not_validated
        
    def load_kobo_data(self):
        try:
            df = pd.read_excel(self.kobo)
            # Further processing of df here
        except Exception as e:
            print(f"Error loading Kobo data: {e}") 
        
        return df

### STARTING WINDOWS
    def open_locations_window(self):
        

        try:
            # Create a new window
            new_window = tk.Toplevel(self.controller)
            new_window.title('Locations window')
            new_window.geometry("400x300")

            # Create a frame for scrollable content
            frame = ttk.Frame(new_window)
            frame.pack(fill=tk.BOTH, expand=True)

            # Add a canvas and scrollbar
            canvas = tk.Canvas(frame)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.configure(yscrollcommand=scrollbar.set)

            # Create another frame inside the canvas
            first_frame = ttk.Frame(canvas)
            canvas.create_window((0, 0), window=first_frame, anchor=tk.NW)

            Main(canvas,"The following Villages are missing in the coordinates file, no checks on the location can be done for these:")
            Main(canvas,print((set(self.df["Village"])-self.villages)))
            Main(canvas,"If you want to add them or adjust the spelling, exit the program now.\n")

            # Button to open a new window
            canvas.new_window_button = tk.Button(self, text="Check locations", command=self.open_new_window(), borderwidth=2, relief="solid")
            canvas.new_window_button.pack(pady=10)

        except Exception as e:
            print(f"Error loading Kobo data: {e}")

    def open_new_window(self):
        # Create a new window
        self.i = self.indexes[self.counter]
        new_window = tk.Toplevel(self.controller)
        new_window.title(f"{self.i} / {self.num_rows}")
        new_window.geometry("1200x800")
        self.new_window = new_window

        # Create a ScrolledFrame widget
        self.scrolled_frame = ScrolledFrame(self.new_window, scrollbars=ScrollbarsType.BOTH,
                                   width=1200, height=800)  # Default width and height
        self.scrolled_frame.pack(side="top", expand=1, fill="both")  # Fill the entire root window

        self.second_frame = self.scrolled_frame.display_widget(tk.Frame)

        if len(set(self.df[self.village_col])-self.villages) > 0:
            Main(self.second_frame,self.lang_dict['validation']['missing_village'][self.language])
            Main(self.second_frame,str(set(self.df[self.village_col])-self.villages))
            Main(self.second_frame,self.lang_dict['validation']['adjust_village'][self.language])
        else:
            pass
        #Add a canvas and scrollbar
        #canvas = tk.Canvas(scrolled_frame)
        #canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #scrollbar_v = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        #scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        #canvas.configure(yscrollcommand=scrollbar_v.set)

        # Create another frame inside the canvas

        #canvas.create_window((0, 0), window=second_frame, anchor=tk.NW)

        # Update scroll region
        #second_frame.update_idletasks()
        #anvas.config(scrollregion=canvas.bbox(tk.ALL))

        # Update scroll region whenever the content changes
        #def on_frame_configure(event):
         #  canvas.configure(scrollregion=canvas.bbox(tk.ALL))

       # second_frame.bind("<Configure>", on_frame_configure)


        # Create destroy button

        destroy_button = tk.Button(self.second_frame, text=self.lang_dict['validation']['button_quit'][self.language], command=lambda: self.quit(new_window))
        destroy_button.pack()
        
        self.start_button_exists = None
        # create start button
        start_button = tk.Button(self.second_frame, text=self.lang_dict['validation']['button_start'][self.language], command=lambda: self.start(self.second_frame,new_window))
        start_button.pack()

### DATE START 
    def start(self,second_frame,new_window):
        if not self.start_button_exists:
  #          if self.df_prev.loc[self.df_prev['_id'] == self.df.loc[self.i, '_id'], ['_validation_status']].empty:
            # initiate containers for everything i'll need in each run
            self.int_Bio_live = tk.IntVar(value=0)
            self.int_Bul_live = tk.IntVar(value=0)
            self.int_Lym_live = tk.IntVar(value=0)
            self.int_Pool_live = tk.IntVar(value=0)
            self.int_Bio_empty = tk.IntVar(value=0)
            self.int_Bul_empty = tk.IntVar(value=0)
            self.int_Lym_empty = tk.IntVar(value=0)
            self.int_Pool_empty = tk.IntVar(value=0)

            # initate containers for frames containing questions, buttons etc.
            self.frame_Bio_live = None
            self.frame_Bul_live = None
            self.frame_Lym_live = None
            self.frame_Pool_live = None
            self.frame_Bio_empty = None
            self.frame_Bul_empty = None
            self.frame_Lym_empty = None
            self.frame_Pool_empty = None

            self.int_dict = {
                'live': {
                    'Biomphalaria': {
                        'information': [self.int_Bio_live, self.lang_dict['validation']['bio_live'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Bio_Error'
                        }
                    },
                    'Bulinus': {
                        'information': [self.int_Bul_live, self.lang_dict['validation']['bul_live'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Bul_Error'
                        }
                    },
                    'Lymnaea': {
                        'information': [self.int_Lym_live, self.lang_dict['validation']['lym_live'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Lym_Error'
                        }
                    },
                    'Pool': {
                        'information': [self.int_Pool_live, self.lang_dict['validation']['pool_live'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Pool_Error'
                        }
                    }
                },
                'empty': {
                    'Biomphalaria': {
                        'information': [self.int_Bio_empty, self.lang_dict['validation']['bio_empty'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Bio_Error'
                        }
                    },
                    'Bulinus': {
                        'information': [self.int_Bul_empty, self.lang_dict['validation']['bul_empty'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Bul_Error'
                        }
                    },
                    'Lymnaea': {
                        'information': [self.int_Lym_empty, self.lang_dict['validation']['lym_empty'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Lym_Error'
                        }
                    },
                    'Pool': {
                        'information': [self.int_Pool_empty, self.lang_dict['validation']['pool_empty'][self.language]],
                        'value': tk.IntVar(value=0),
                        'error': {
                            'column': 'Pool_Error'
                        }
                    }
                }
            }

            self.submission_counter = 0             
            self.errors_dict = {
            self.lang_dict['validation']['error_date'][self.language]: 'OK',
            self.lang_dict['validation']['error_location'][self.language]: 'OK',
            self.lang_dict['validation']['error_distance'][self.language]: 'OK',
            self.lang_dict['validation']['error_scoop'][self.language]: 'OK',
            self.lang_dict['validation']['error_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_bio_live_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_bul_live_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_lym_live_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_pool_live_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_bio_empty_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_bul_empty_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_lym_empty_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_pool_empty_images'][self.language]: 'OK',
            self.lang_dict['validation']['error_counting'][self.language]: 'OK',
            self.lang_dict['validation']['error_liveempty'][self.language]: 'OK',
            self.lang_dict['validation']['error_identification'][self.language]: 'OK',
            self.lang_dict['validation']['error_bio'][self.language]: 'OK',
            self.lang_dict['validation']['error_bul'][self.language]: 'OK',
            self.lang_dict['validation']['error_lym'][self.language]: 'OK',
            self.lang_dict['validation']['error_pool'][self.language]: 'OK',
            }
            # Check date
            date_str = str(self.df.loc[self.i,self.date_col])   
            try: 
                date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date()
                tester = self.is_date_realistic(date_obj)
                
                if not tester:
                    self.errors_dict[self.lang_dict['validation']['error_date'][self.language]] = self.lang_dict['validation']['warning_date_realistic'][self.language]
                    self.df.loc[self.i, 'Date_warning'] = 1
            except:
                    self.errors_dict[self.lang_dict['validation']['error_date'][self.language]] = self.lang_dict['validation']['warning_date_format'][self.language]
                    self.df.loc[self.i, 'Date_warning'] = 1
                
            
            #start up destroy button flag for later
            self.destroy_button_exists = None
            self.empty_check_button = None
            self.living_check_button = None

            # Check locations 
            if(self.df.iloc[self.i][self.village_col] not in self.villages):
                self.df.loc[self.i,'Location_Error'] = 1
                self.errors_dict[self.lang_dict['validation']['error_location'][self.language]] = self.lang_dict['validation']['warning_location'][self.language]

            else:
                # location is present in our coordinates data
                x_dist = self.df.loc[self.i,self.longitude_col] - self.coordinates_df.loc[self.coordinates_df['Name village'] == self.df.loc[self.i,self.village_col],['Fixed site Longitute']]
                y_dist = self.df.loc[self.i,self.latitude_col] - self.coordinates_df.loc[self.coordinates_df['Name village'] == self.df.loc[self.i,self.village_col],['Fixed site Latitude ']]

                if abs(x_dist.iloc[0,0]) > self.Dmax_x or abs(y_dist.iloc[0,0]) > self.Dmax_y :
                    self.df.loc[self.i, 'Distance_Error'] = 1
                    self.errors_dict[self.lang_dict['validation']['error_distance'][self.language]] = self.lang_dict['validation']['warning_distance'][self.language]


                else:
                    pass
            
            #CHECKING SCOOP-TIME
            self.start_collection = pd.to_datetime(self.df.loc[self.i,self.start_sampling])
            self.stop_collection = pd.to_datetime(self.df.loc[self.i,self.end_sampling])
            duration = self.stop_collection - self.start_collection

            if duration < self.tmin or duration > self.tmax:
                self.df.loc[self.i,'Scoop_Time_Error'] = 1
                self.errors_dict[self.lang_dict['validation']['error_scoop'][self.language]] = self.lang_dict['validation']['warning_scoop'][self.language]



            else:
                pass

            ### CHECK LIVE & EMPTY
            self.live = 1
            self.empty = 1
            if (self.df.loc[self.i,self.any_snails_found] == self.any_found_no) or (
                self.df.loc[self.i,self.which_snails_found] == self.just_empty):

                # Nothing or only empty shells:
                self.live = 0
                self.df.loc[self.i,self.live_bul_q] = 0
                self.df.loc[self.i,self.live_bio_q] = 0
                self.df.loc[self.i,self.live_lym_q] = 0
                self.df.loc[self.i,self.live_pool_q] = 0

            if (self.df.loc[self.i,self.any_snails_found] == self.any_found_no) or (
                self.df.loc[self.i,self.which_snails_found] == self.just_live):
                # Nothing or only live snails:
                self.empty = 0
                self.df.loc[self.i,self.empty_bul_q] = 0
                self.df.loc[self.i,self.empty_bio_q] = 0
                self.df.loc[self.i,self.empty_lym_q] = 0
                self.df.loc[self.i,self.empty_pool_q] = 0

            self.vivs_empty_tree(second_frame)
            
            #ensure repeated pressing will not cause buttons to duplicate
            self.start_button_exists = 1
    
    ### SOME AUTOMATIC CHECKS 
    def is_date_realistic(self,date_obj):
        # Check if the date is within a realistic range (e.g., 1900 to 2100)
        start_date = self.start_date
        end_date = self.end_date
        return start_date <= date_obj <= end_date     

### GO INTO PICTURES
    def vivs_empty_tree(self,second_frame):
        self.second_frame = second_frame
        self.Bio_live = tk.IntVar(value=0)
        self.Bul_live = tk.IntVar(value=0)
        self.Lym_live = tk.IntVar(value=0)
        self.Pool_live = tk.IntVar(value=0)
        self.Bio_empty = tk.IntVar(value=0)
        self.Bul_empty = tk.IntVar(value=0)
        self.Lym_empty = tk.IntVar(value=0)
        self.Pool_empty = tk.IntVar(value=0)
        if self.live == 0 and self.empty == 0:
            Main(self.second_frame,self.lang_dict['validation']['no_snails_warning'][self.language],color = 'green')
            print_erros(self)
            destroy_this_button(self)

        elif self.live == 0 and self.empty == 1:
            start_check(self,second_frame)

        elif self.live == 1 and self.empty == 0:
            start_check(self,second_frame)

        else: 
            start_check(self,second_frame)

    def quit(self, new_window):
        new_window.destroy()

    def get_language(self):
        return self.language
    
    def get_lang_dict(self):
        return self.lang_dict

    def update_values_langdict(self, lang, dict):
        self.language = lang
        self.lang_dict = dict

