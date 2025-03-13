import tkinter as tk
from PIL import Image, ImageTk
from os import path
from aesthetics.text import Main  # Assuming Main class is defined in aesthetics.text module
import pandas as pd
import os.path

def start_check(self,second_frame):
    self.second_frame = second_frame
    real_check(self)

# initiate checking
def real_check(self):

    # inittiate containers for final counts    
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
                'information': [self.int_Bio_live, self.lang_dict['validation']['bio_live'][self.language], 'bio_live', 'error_bio'],
                'image': 'error_bio_live_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Bio_Error',
                    'image': 'Bio_Live_Image_Missing'
                }
            },
            'Bulinus': {
                'information': [self.int_Bul_live, self.lang_dict['validation']['bul_live'][self.language], 'bul_live','error_bul'],
                'image': 'error_bul_live_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Bul_Error',
                    'image': 'Bul_Live_Image_Missing'
                }
            },
            'Lymnaea': {
                'information': [self.int_Lym_live, self.lang_dict['validation']['lym_live'][self.language], 'lym_live','error_lym'],
                'image': 'error_lym_live_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Lym_Error',
                    'image': 'Lym_Live_Image_Missing'
                }
            },
            'Pool': {
                'information': [self.int_Pool_live, self.lang_dict['validation']['pool_live'][self.language], 'pool_live','error_pool'],
                'image': 'error_pool_live_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Pool_Error',
                    'image': 'Pool_Live_Image_Missing'
                }
            }
        },
        'empty': {
            'Biomphalaria': {
                'information': [self.int_Bio_empty, self.lang_dict['validation']['bio_empty'][self.language],'bio_empty','error_bio'],
                'image': 'error_bio_empty_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Bio_Error',
                    'image': 'Bio_Empty_Image_Missing'
                }
            },
            'Bulinus': {
                'information': [self.int_Bul_empty, self.lang_dict['validation']['bul_empty'][self.language],'bul_empty','error_bul'],
                'image': 'error_bul_empty_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Bul_Error',
                    'image': 'Bul_Empty_Image_Missing'
                }
            },
            'Lymnaea': {
                'information': [self.int_Lym_empty, self.lang_dict['validation']['lym_empty'][self.language],'lym_empty','error_lym'],
                'image': 'error_lym_empty_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Lym_Error',
                    'image': 'Lym_Empty_Image_Missing'
                }
            },
            'Pool': {
                'information': [self.int_Pool_empty, self.lang_dict['validation']['pool_empty'][self.language],'pool_empty','error_pool'],
                'image': 'error_pool_empty_images',
                'value': tk.IntVar(value=0),
                'error': {
                    'column': 'Pool_Error',
                    'image': 'Pool_Empty_Image_Missing'
                }
            }
        }
    }

    self.submission_counter = 0
    for liveempty in ['live','empty']:
        for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
            q_key, im_key, print_key, error_key, frame_key_placeholder, int_key  = get_type_details(self,liveempty,type)

            if self.df.loc[self.i,q_key] > 0:

                p = os.path.join(self.image,str(self.df.loc[self.i,im_key]))
                print(p)

                if path.exists(p):
                    frame_key = display_image(self,p,frame_key_placeholder)
                    frame_key.live_or_empty = liveempty
                    frame_key.species = type
                    frame_key.submission = None
                    frame_key.int_dict = {
                        'live': {
                            'Biomphalaria': {
                                'information': [self.int_Bio_live, self.lang_dict['validation']['bio_live'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Bulinus': {
                                'information': [self.int_Bul_live, self.lang_dict['validation']['bul_live'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Lymnaea': {
                                'information': [self.int_Lym_live, self.lang_dict['validation']['lym_live'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Pool': {
                                'information': [self.int_Pool_live, self.lang_dict['validation']['pool_live'][self.language]],
                                'value': tk.IntVar(value=0)
                            }
                        },
                        'empty': {
                            'Biomphalaria': {
                                'information': [self.int_Bio_empty, self.lang_dict['validation']['bio_empty'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Bulinus': {
                                'information': [self.int_Bul_empty, self.lang_dict['validation']['bul_empty'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Lymnaea': {
                                'information': [self.int_Lym_empty, self.lang_dict['validation']['lym_empty'][self.language]],
                                'value': tk.IntVar(value=0)
                            },
                            'Pool': {
                                'information': [self.int_Pool_empty, self.lang_dict['validation']['pool_empty'][self.language]],
                                'value': tk.IntVar(value=0)
                            }
                        }
                    }

                    pack_original_count(self,
                                        q_key,
                                        im_key,
                                        print_key,
                                        error_key,
                                        frame_key,
                                        int_key,
                                        type)                   
                else:
                    else_function(self, frame_key_placeholder, liveempty, type)

def else_function(self, frame_key_placeholder,liveempty,type):
    text = self.lang_dict['checking']['image_missing_text'][self.language] + self.int_dict[liveempty][type]['information'][1]

    self.submission_counter += 1

    # general warning 
    self.df.loc[self.i,'Images_Missing'] = 1
    self.errors_dict[self.lang_dict['validation']['error_images'][self.language]] = self.lang_dict['validation']['no_image_warning'][self.language]

    # species specific warning 
    error_col = self.int_dict[liveempty][type]['error']['image']
    self.df.loc[self.i,error_col] = 1 
    # species specific logging
    error_log = self.int_dict[liveempty][type]['image']
    self.errors_dict[self.lang_dict['validation'][error_log][self.language]] = text

    # set to NA 
    if self.int_dict[liveempty][type]['value'].get() == 0:
        self.int_dict[liveempty][type]['value'].set(999)
    else:
        pass
    
    frame_key_image_missing = get_frame(self,frame_key_placeholder)
    Main(frame_key_image_missing,text)

    frame_key_image_missing.int_dict = {
        'live': {
            'Biomphalaria': {
                'information': [self.int_Bio_live, self.lang_dict['validation']['bio_live'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Bulinus': {
                'information': [self.int_Bul_live, self.lang_dict['validation']['bul_live'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Lymnaea': {
                'information': [self.int_Lym_live, self.lang_dict['validation']['lym_live'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Pool': {
                'information': [self.int_Pool_live, self.lang_dict['validation']['pool_live'][self.language]],
                'value': tk.IntVar(value=0)
            }
        },
        'empty': {
            'Biomphalaria': {
                'information': [self.int_Bio_empty, self.lang_dict['validation']['bio_empty'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Bulinus': {
                'information': [self.int_Bul_empty, self.lang_dict['validation']['bul_empty'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Lymnaea': {
                'information': [self.int_Lym_empty, self.lang_dict['validation']['lym_empty'][self.language]],
                'value': tk.IntVar(value=0)
            },
            'Pool': {
                'information': [self.int_Pool_empty, self.lang_dict['validation']['pool_empty'][self.language]],
                'value': tk.IntVar(value=0)
            }
        }
    }

    frame_key_image_missing.live_or_empty = liveempty
    frame_key_image_missing.species = type
    frame_key_image_missing.submission = None
    
    error = None
    frame_key_image_missing.submit_flag = None
    frame_key_image_missing.submit_button = None
    frame_key_image_missing.submit_button  = tk.Button(frame_key_image_missing, text=self.lang_dict['checking']['submit'][self.language], command=lambda: submit(self,error,frame_key_image_missing), foreground='black')
    frame_key_image_missing.submit_button.pack(anchor = 'w')

def get_frame(self,frame_key):
    self.imageframe = tk.Frame(self.second_frame)
    self.imageframe.pack(fill='x', pady=10)  # Create a new frame for each image and its associated content
    # Create another frame for the questions and buttons on the right side
    self.questionframe = tk.Frame(self.imageframe)
    self.questionframe.pack() 
    frame_key = self.questionframe
    return frame_key

# get required texts, buttons etc.
def get_type_details(self,liveempty,type):
    if liveempty == 'empty':
        if type == "Biomphalaria":
            return self.empty_bio_q, self.empty_bio_img, self.lang_dict['validation']['bio_empty'][self.language], 'Bio_Error',self.frame_Bio_empty,self.int_Bio_empty
        elif type == "Bulinus":
            return self.empty_bul_q, self.empty_bul_img, self.lang_dict['validation']['bul_empty'][self.language], 'Bul_Error',self.frame_Bul_empty,self.int_Bul_empty
        elif type == "Lymnaea":
            return self.empty_lym_q, self.empty_lym_img, self.lang_dict['validation']['lym_empty'][self.language], 'Lym_Error',self.frame_Lym_empty,self.int_Lym_empty
        elif type == "Pool":
            return self.empty_pool_q, self.empty_pool_img, self.lang_dict['validation']['pool_empty'][self.language], 'Pool_Error',self.frame_Pool_empty,self.int_Pool_empty
        else:
            pass
    elif liveempty == 'live':
        if type == "Biomphalaria":
            return self.live_bio_q, self.live_bio_img, self.lang_dict['validation']['bio_live'][self.language], 'Bio_Error',self.frame_Bio_live,self.int_Bio_live
        elif type == "Bulinus":
            return self.live_bul_q, self.live_bul_img, self.lang_dict['validation']['bul_live'][self.language], 'Bul_Error',self.frame_Bul_live,self.int_Bul_live
        elif type == "Lymnaea":
            return self.live_lym_q, self.live_lym_img, self.lang_dict['validation']['lym_live'][self.language], 'Lym_Error',self.frame_Lym_live,self.int_Lym_live
        elif type == "Pool":
            return self.live_pool_q, self.live_pool_img, self.lang_dict['validation']['pool_live'][self.language], 'Pool_Error',self.frame_Pool_live,self.int_Pool_live
        else:
            pass

# image displayer, this will pack the original image and create the frame for questions  
def display_image(self, path, frame_key):
    self.imageframe = tk.Frame(self.second_frame)
    self.imageframe.pack(fill='x', pady=10)  # Create a new frame for each image and its associated content

    # Load and display the image on the left side of the frame
    image = Image.open(path)
    # Get image dimensions
    width, height = image.size

    # Rotate the image if width is greater than height
    if width > height:
        rotated_image = image.rotate(90, expand=True)
    else:
        rotated_image = image

    rotated_image = resize_image(rotated_image, 0.2)  # Resize the image to fit in the window
    photo = ImageTk.PhotoImage(rotated_image)
    image_label = tk.Label(self.imageframe, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack(side='left')  # Pad the image label

    # Create another frame for the questions and buttons on the right side
    self.questionframe = tk.Frame(self.imageframe)
    self.questionframe.pack(side='right') 
    frame_key = self.questionframe
    return frame_key

# image resizer 
def resize_image(image, scale_factor):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

# this will pack the actual  questions 
def pack_original_count(self, q_key, im_key, print_key, error_key, frame_key, int_key,shell_type):
    self.submission_counter += 1
    
    text = self.lang_dict['checking']['q1'][self.language] + shell_type + '?'
    Main(frame_key, text)

    frame_key.q1_flag = None
    frame_key.q1_yes_button = None 
    frame_key.q1_no_button = None
    frame_key.q_key = q_key
    frame_key.q1_yes_button  = tk.Button(frame_key, text=self.lang_dict['checking']['yes'][self.language], command=lambda: q1_yes(self,error_key,frame_key), foreground='black')
    frame_key.q1_yes_button .pack(anchor = 'w')
    
    frame_key.q1_no_button = tk.Button(frame_key, text=self.lang_dict['checking']['no'][self.language], command=lambda: q1_no(self,error_key,frame_key), foreground='black')
    frame_key.q1_no_button.pack(anchor = 'w')

# options for buttons / in questionframe
# CLASSIFIED CORRECTLY 
def q1_yes(self,error,frame_key):
    frame_key.q1_yes_button.config(foreground='blue')
    frame_key.q1_no_button.config(foreground='black')


    if frame_key.live_or_empty == 'live':
        text_q2 = self.lang_dict['checking']['q2_empty'][self.language]
    elif frame_key.live_or_empty == 'empty':
        text_q2 = self.lang_dict['checking']['q2_live'][self.language]

    if not frame_key.q1_flag:
        
        Main(frame_key, text_q2)

        frame_key.q2_flag = None
        frame_key.q2_yes_button = None 
        frame_key.q2_no_button = None
        frame_key.q2_yes_button  = tk.Button(frame_key, text=self.lang_dict['checking']['yes'][self.language], command=lambda: q2_yes(self,error,frame_key), foreground='black')
        frame_key.q2_yes_button.pack(anchor = 'w')
        
        frame_key.q2_no_button = tk.Button(frame_key, text=self.lang_dict['checking']['no'][self.language], command=lambda: q2_no(self,error,frame_key), foreground='black')
        frame_key.q2_no_button.pack(anchor = 'w')
        
        frame_key.q1_flag = 1

# SHELLS OR LIVING OF SAME INDIVIDUAL IN WRONG IMAGE 
def q2_yes(self,error,frame_key):
    frame_key.q2_yes_button.config(foreground='blue')
    frame_key.q2_no_button.config(foreground='black')
    self.df.loc[self.i,'Shells_Error'] = 1
    self.errors_dict[self.lang_dict['validation']['error_liveempty'][self.language]] = self.lang_dict['validation']['warning_liveempty'][self.language]

    if not frame_key.q2_flag:

        # input empty or live shells
        if frame_key.live_or_empty == 'live':
            text_input = self.lang_dict['checking']['input_empty'][self.language]
            frame_key.opposite = frame_key.int_dict['empty'][frame_key.species]['value']

        elif frame_key.live_or_empty == 'empty':
            text_input = self.lang_dict['checking']['input_live'][self.language]
            frame_key.opposite = frame_key.int_dict['live'][frame_key.species]['value']
        
        #print the question
        Main(frame_key, text_input)
        # Create an Entry widget
        frame_key.entry_key = tk.Entry(frame_key, textvariable=frame_key.opposite, width=40)
        frame_key.entry_key.pack(anchor = 'w')
        
        # is the original count correct
        Main(frame_key, self.lang_dict['checking']['original_count'][self.language] + self.int_dict[frame_key.live_or_empty][frame_key.species]['information'][1] + ' = ' + str(int(float(self.df.loc[self.i, frame_key.q_key]))) + self.lang_dict['checking']['correct?'][self.language])

        frame_key.q3_flag = None
        frame_key.q3_yes_button = None 
        frame_key.q3_no_button = None
        frame_key.q3_yes_button  = tk.Button(frame_key, text=self.lang_dict['checking']['yes'][self.language], command=lambda: q3_yes(self,error,frame_key), foreground='black')
        frame_key.q3_yes_button.pack(anchor = 'w')
        frame_key.q3_no_button = tk.Button(frame_key, text=self.lang_dict['checking']['no'][self.language], command=lambda: q3_no(self,error,frame_key), foreground='black')
        frame_key.q3_no_button.pack(anchor = 'w')
        
        self.errors.append('')

        frame_key.q2_flag = 1

# NO LIVING OR SHELLS OF SAME INDIVIDUAL IN THE WRONG IMAGE 
def q2_no(self, error, frame_key):
    frame_key.q2_no_button.config(foreground='blue')
    frame_key.q2_yes_button.config(foreground='black')

    if not frame_key.q2_flag:
        # count correct? 
        Main(frame_key, self.lang_dict['checking']['original_count'][self.language] + self.int_dict[frame_key.live_or_empty][frame_key.species]['information'][1] + ' = ' + str(int(float(self.df.loc[self.i, frame_key.q_key]))) + self.lang_dict['checking']['correct?'][self.language])

        frame_key.q3_flag = None
        frame_key.q3_yes_button = None 
        frame_key.q3_no_button = None
        frame_key.q3_yes_button  = tk.Button(frame_key, text=self.lang_dict['checking']['yes'][self.language], command=lambda: q3_yes(self,error,frame_key), foreground='black')
        frame_key.q3_yes_button.pack(anchor = 'w')
        frame_key.q3_no_button = tk.Button(frame_key, text=self.lang_dict['checking']['no'][self.language], command=lambda: q3_no(self,error,frame_key), foreground='black')
        frame_key.q3_no_button.pack(anchor = 'w')

        frame_key.q2_flag = 1

def q3_yes(self, error, frame_key):
    frame_key.q3_yes_button.config(foreground='blue')
    frame_key.q3_no_button.config(foreground='black')

    if not frame_key.q3_flag:
        frame_key.int_dict[frame_key.live_or_empty][frame_key.species]['value'].set(int(float(self.df.loc[self.i, frame_key.q_key])))

        frame_key.submit_flag = None
        frame_key.submit_button = None
        frame_key.submit_button  = tk.Button(frame_key, text=self.lang_dict['checking']['submit'][self.language], command=lambda: submit(self,error,frame_key), foreground='black')
        frame_key.submit_button.pack(anchor = 'w')

        frame_key.q3_flag = 1

def q3_no(self, error, frame_key):
    frame_key.q3_no_button.config(foreground='blue')
    frame_key.q3_yes_button.config(foreground='black')

    if not frame_key.q3_flag:
        self.df.loc[self.i, 'Counting_Error'] = 1
        self.errors_dict[self.lang_dict['validation']['error_counting'][self.language]] = self.lang_dict['validation']['warning_counting'][self.language]
        
        # Create an Entry widget
        if frame_key.live_or_empty == 'live':
            text_input = self.lang_dict['checking']['input_correct_number_live'][self.language]
            frame_key.same = frame_key.int_dict['live'][frame_key.species]['value']

        elif frame_key.live_or_empty == 'empty':
            text_input = self.lang_dict['checking']['input_correct_number_empty'][self.language]
            frame_key.same = frame_key.int_dict['empty'][frame_key.species]['value']

        Main(frame_key, text_input)

        entry_key = tk.Entry(frame_key, textvariable=frame_key.same, width=40)
        entry_key.pack(anchor = 'w')

        frame_key.submit_flag = None
        frame_key.submit_button = None
        frame_key.submit_button  = tk.Button(frame_key, text=self.lang_dict['checking']['submit'][self.language], command=lambda: submit(self,error,frame_key), foreground='black')
        frame_key.submit_button.pack(anchor = 'w')

        frame_key.q3_flag = 1

# CLASSIFIED INCORRECTLY 
def q1_no(self,error,frame_key):
    frame_key.q1_no_button.config(foreground='blue')
    frame_key.q1_yes_button.config(foreground='black')
    self.df.loc[self.i,'Identification_Error'] = 1
    self.errors_dict[self.lang_dict['validation']['error_identification'][self.language]] = self.lang_dict['validation']['warning_identification'][self.language]

    error = self.int_dict[frame_key.live_or_empty][frame_key.species]['error']['column']
    self.df.loc[self.i,error] = 1
    this_key = self.int_dict[frame_key.live_or_empty][frame_key.species]['information'][3]
    self.errors_dict[self.lang_dict['validation'][this_key][self.language]] = self.lang_dict['validation']['warning_species_identification'][self.language]


    if not frame_key.q1_flag:
        if frame_key.live_or_empty == 'live':
            text_q4 = self.lang_dict['checking']['q2_empty'][self.language]
        elif frame_key.live_or_empty == 'empty':
            text_q4 = self.lang_dict['checking']['q2_live'][self.language]
        
        Main(frame_key, text_q4)

        frame_key.q4_flag = None
        frame_key.q4_yes_button = None 
        frame_key.q4_no_button = None
        frame_key.q4_yes_button  = tk.Button(frame_key, text=self.lang_dict['checking']['yes'][self.language], command=lambda: q4_yes(self,error,frame_key), foreground='black')
        frame_key.q4_yes_button.pack(anchor = 'w')
        
        frame_key.q4_no_button = tk.Button(frame_key, text=self.lang_dict['checking']['no'][self.language], command=lambda: q4_no(self,error,frame_key), foreground='black')
        frame_key.q4_no_button.pack(anchor = 'w')
        
        frame_key.q1_flag = 1

def q4_yes(self,error,frame_key):
    frame_key.q4_yes_button.config(foreground='blue')
    frame_key.q4_no_button.config(foreground='black')
    self.df.loc[self.i,'Shells_Error'] = 1
    self.errors_dict[self.lang_dict['validation']['error_liveempty'][self.language]] = self.lang_dict['validation']['warning_liveempty'][self.language]


    if not frame_key.q4_flag:

        if frame_key.live_or_empty == 'live':
            text_q4 = self.lang_dict['checking']['input_empty'][self.language]
            frame_key.opposite = 'empty'

        elif frame_key.live_or_empty == 'empty':
            text_q4 = self.lang_dict['checking']['input_live'][self.language]
            frame_key.opposite = 'live'

        Main(frame_key, text_q4)

        for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
            text = frame_key.int_dict[frame_key.opposite][type]['information'][1]
            int_key = frame_key.int_dict[frame_key.opposite][type]['value']

            frame_key.label = tk.Label(frame_key, text=text)
            frame_key.label.pack()
            # Create an Entry widget

            frame_key.live_entry = tk.Entry(frame_key, textvariable=int_key, width=40)
            frame_key.live_entry.pack()
        
        if frame_key.live_or_empty == 'live':
            text_q4 = self.lang_dict['checking']['input_live'][self.language]
        elif frame_key.live_or_empty == 'empty':
            text_q4 = self.lang_dict['checking']['input_empty'][self.language]

        Main(frame_key, text_q4)

        for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
            text = frame_key.int_dict[frame_key.live_or_empty][type]['information'][1]

            int_key = frame_key.int_dict[frame_key.live_or_empty][type]['value']

            frame_key.label = tk.Label(frame_key, text=text)
            frame_key.label.pack()
            # Create an Entry widget

            frame_key.live_entry = tk.Entry(frame_key, textvariable=int_key, width=40)
            frame_key.live_entry.pack()
        
        frame_key.submit_flag = None
        frame_key.submit_button = None
        frame_key.submit_button  = tk.Button(frame_key, text=self.lang_dict['checking']['submit'][self.language], command=lambda: submit(self,error,frame_key), foreground='black')
        frame_key.submit_button.pack(anchor = 'w')


        frame_key.q4_flag = 1 

def q4_no(self,error,frame_key):
    frame_key.q4_yes_button.config(foreground='blue')
    frame_key.q4_no_button.config(foreground='black')

    if not frame_key.q4_flag:
        if frame_key.live_or_empty == 'live':
            text_q4 = self.lang_dict['checking']['input_live'][self.language]
        elif frame_key.live_or_empty == 'empty':
            text_q4 = self.lang_dict['checking']['input_empty'][self.language]

        Main(frame_key, text_q4)

        for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
            text = frame_key.int_dict[frame_key.live_or_empty][type]['information'][1]
            int_key = frame_key.int_dict[frame_key.live_or_empty][type]['value']

            frame_key.label = tk.Label(frame_key, text=text)
            frame_key.label.pack()
            # Create an Entry widget

            frame_key.live_entry = tk.Entry(frame_key, textvariable=int_key, width=40)
            frame_key.live_entry.pack()
        
        frame_key.submit_flag = None
        frame_key.submit_button = None
        frame_key.submit_button  = tk.Button(frame_key, text=self.lang_dict['checking']['submit'][self.language], command=lambda: submit(self,error,frame_key), foreground='black')
        frame_key.submit_button.pack(anchor = 'w')

        frame_key.q4_flag = 1   



def submit(self,error,frame_key):
    frame_key.submit_button.config(foreground='blue') 

    if not frame_key.submission:
        for liveempty in ['live','empty']:
            for species in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
                
                # set to zero is NA (from missing picture) needs to be adjusted to a value (found in another picture)
                if self.int_dict[liveempty][species]['value'].get() == 999 and frame_key.int_dict[liveempty][species]['value'].get() > 0:
                    self.int_dict[liveempty][species]['value'].set(0)

                self.int_dict[liveempty][species]['value'].set(self.int_dict[liveempty][species]['value'].get() + frame_key.int_dict[liveempty][species]['value'].get())
        
        self.submission_counter += -1

        if self.submission_counter == 0:
            check_for_corrections(self)

        frame_key.submission = 1 

# CHECK CORRECTIONS 
def check_for_corrections(self):
    # Update live counts directly from Entry widgets
    """
    if self.entry_Bio_live:
        self.Bio_live = int(float(self.entry_Bio_live.get().strip()))
    if self.entry_Bul_live:
        self.Bul_live = int(float(self.entry_Bul_live.get().strip()))
    if self.entry_Lym_live:
        self.Lym_live = int(float(self.entry_Lym_live.get().strip()))
    if self.entry_Pool_live:
        self.Pool_live = int(float(self.entry_Pool_live.get().strip()))

    # Update empty counts directly from Entry widgets
    if self.entry_Bio_empty:
        self.Bio_empty = int(float(self.entry_Bio_empty.get().strip()))
    if self.entry_Bul_empty:
        self.Bul_empty = int(float(self.entry_Bul_empty.get().strip()))
    if self.entry_Lym_empty:
        self.Lym_empty = int(float(self.entry_Lym_empty.get().strip()))
    if self.entry_Pool_empty:
        self.Pool_empty = int(float(self.entry_Pool_empty.get().strip()))
    """
    self.entry_Bio_live2 = None
    self.entry_Bul_live2 = None
    self.entry_Lym_live2 = None
    self.entry_Pool_live2 = None
    self.entry_Bio_empty2 = None
    self.entry_Bul_empty2 = None
    self.entry_Lym_empty2 = None
    self.entry_Pool_empty2 = None

    #if self.df.loc[self.i, "Bio_Error"] == 1 or self.df.loc[self.i, "Bul_Error"] == 1 or self.df.loc[self.i, "Lym_Error"] == 1 or self.df.loc[self.i, "Pool_Error"] == 1:
        # There was an error in the counting of the snails, we will try and correct this now:
    check_live = 0
    for q_key in [self.live_bio_q,self.live_bul_q,self.live_lym_q,self.live_pool_q]:
        if self.df.loc[self.i,q_key] > 0:
            check_live = 1
        else: 
            pass

    if check_live == 1:
        p = os.path.join(self.image,str(self.df.loc[self.i,self.img_living]))
        if path.exists(p):
            self.imageframe = tk.Frame(self.second_frame)
            self.imageframe.pack(fill='x', pady=10)

            Main(self.second_frame, self.lang_dict['checking']['adjust_live'][self.language])
            display_image(self,p,self.imageframe)

            self.questionframe = tk.Frame(self.imageframe)
            self.questionframe.pack(side='right') 

            for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
                live_text, live_el, live_entry, _, _, _ = get_details(self,type)
                # Create a Label widget
                el = self.int_dict['live'][type]['value'] 
                key = self.int_dict['live'][type]['information'][2] 
                text = self.lang_dict['validation'][key][self.language]

                label = tk.Label(self.questionframe, text=text)
                label.pack()
                # Create an Entry widget

                live_entry = tk.Entry(self.questionframe, textvariable=el, width=40)
                live_entry.pack()

        else:
            Main(self.second_frame,self.lang_dict['checking']['live_missing'][self.language])
            self.df.loc[self.i,'Images_Missing'] = 1
            self.errors_dict[self.lang_dict['validation']['error_images'][self.language]] = self.lang_dict['validation']['no_image_warning'][self.language]
    
    else:
        pass

    # then empty
    check_empty = 0
    for q_key in [self.empty_bio_q,self.empty_bul_q,self.empty_lym_q,self.empty_pool_q]:
        if self.df.loc[self.i,q_key] > 0:
            check_empty = 1
        else: 
            pass        
    
    if check_empty == 1:
        p = os.path.join(self.image,str(self.df.loc[self.i,self.img_empty]))
        if path.exists(p):
            self.imageframe2 = tk.Frame(self.second_frame)
            self.imageframe2.pack(fill='x', pady=10)

            Main(self.second_frame, self.lang_dict['checking']['adjust_empty'][self.language])
            display_image(self,p,self.imageframe)

            self.questionframe2 = tk.Frame(self.imageframe2)
            self.questionframe2.pack(side='right') 

            for type in ['Biomphalaria','Bulinus','Lymnaea','Pool']:
                live_text, live_el, live_entry, _, _, _ = get_details(self,type)
                # Create a Label widget
                el = self.int_dict['empty'][type]['value'] 
                key = self.int_dict['empty'][type]['information'][2] 
                text = self.lang_dict['validation'][key][self.language]

                label = tk.Label(self.questionframe, text=text)
                label.pack()
                # Create an Entry widget

                live_entry = tk.Entry(self.questionframe, textvariable=el, width=40)
                live_entry.pack()
            
        else:
            Main(self.second_frame,self.lang_dict['checking']['empty_missing'][self.language])
            self.df.loc[self.i,'Images_Missing'] = 1
            self.errors_dict[self.lang_dict['validation']['error_images'][self.language]] = self.lang_dict['validation']['no_image_warning'][self.language]

    else:
        pass

    print_erros(self)

    destroy_this_button(self)

### DESTROY WINDOWS
def destroy_this_button(self):
    if not self.destroy_button_exists:
        Main(self.second_frame,self.lang_dict['checking']['record_finished'][self.language])
        destroy_button = tk.Button(self.second_frame, text=self.lang_dict['checking']['quit_save'][self.language], command=lambda: destroy_window(self))
        destroy_button.pack()
        # ensure double pressing doesnt duplicate buttons
        self.destroy_button_exists = 1

def destroy_window(self):
    mode = 1 #0 for testing, 1 for regular
    self.df.loc[self.i,'_validation_status'] = mode
    ##ADD CHECKED PROTOCOL TO PREVIOUS DATAFRAME
            ## Add the corrected values to the columns:

    self.df.loc[self.i, 'Bio_live_corrected'] = self.int_dict['live']['Biomphalaria']['value'].get()
    self.df.loc[self.i, 'Bul_live_corrected'] = self.int_dict['live']['Bulinus']['value'].get()
    self.df.loc[self.i, 'Lym_live_corrected'] = self.int_dict['live']['Lymnaea']['value'].get()
    self.df.loc[self.i, 'Pool_live_corrected'] = self.int_dict['live']['Pool']['value'].get()
    self.df.loc[self.i, 'Bio_empty_corrected'] = self.int_dict['empty']['Biomphalaria']['value'].get()
    self.df.loc[self.i, 'Bul_empty_corrected'] = self.int_dict['empty']['Bulinus']['value'].get()
    self.df.loc[self.i, 'Lym_empty_corrected'] = self.int_dict['empty']['Lymnaea']['value'].get()
    self.df.loc[self.i, 'Pool_empty_corrected'] = self.int_dict['empty']['Pool']['value'].get() 
    self.df.loc[self.i, 'Validation_by'] = self.name_entry.get()
    self.df.loc[self.i, 'Validation_date'] = self.date_current


    self.df_prev = pd.concat([self.df_prev,pd.DataFrame([self.df.loc[self.i,:]])], sort=False)          
    self.df.to_excel(self.kobo,index = False)
    self.df_prev.to_excel(self.new,index = False)
    self.new_window.destroy()
    self.counter += 1
    self.start_button_exists = None
    self.destroy_button_exists = None
    print(f"Window destroyed. Counter updated to: {self.counter}")
    self.open_new_window()

# get required text, buttons etc. 
def get_details(self,type):
        if type == "Biomphalaria":
            return self.lang_dict['validation']['bio_live'][self.language], self.Bio_live, self.entry_Bio_live2, self.lang_dict['validation']['bio_empty'][self.language], self.Bio_empty, self.entry_Bio_empty2
        if type == "Bulinus":
            return self.lang_dict['validation']['bul_live'][self.language], self.Bul_live, self.entry_Bul_live2, self.lang_dict['validation']['bul_empty'][self.language], self.Bul_empty, self.entry_Bul_empty2 
        if type == "Lymnaea":
            return self.lang_dict['validation']['lym_live'][self.language], self.Lym_live,self.entry_Lym_live2, self.lang_dict['validation']['lym_empty'][self.language], self.Lym_empty, self.entry_Lym_empty2         
        if type == "Pool":
            return self.lang_dict['validation']['pool_live'][self.language], self.Pool_live, self.entry_Pool_live2, self.lang_dict['validation']['pool_empty'][self.language], self.Pool_empty, self.entry_Pool_empty2

def print_erros(self):
    for key, value in self.errors_dict.items():
        if value == 'OK':
            Main(self.second_frame,f"{key}: {value}")
        else:
            Main(self.second_frame,f"{key}: {value}",color = 'red')


