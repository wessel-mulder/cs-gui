import tkinter as tk
from pages.start import StartPage
from pages.data import DataDescriptionPage
from pages.previous import PreviousPage
from pages.validation import ValidationPage

dictionary = {
    'start': {
        'welcome': {
            'en': 'Welcome to the snail detector!',
            'fr': 'Bienvenue au détecteur des escargots!'
        },
        'intro_text': {
            'en': "",
            'fr': ""
        },
        'start_button': {
            'en': 'Are you ready to get started?',
            'fr': 'Etes-vous prêt à commencer?'
        },
        'language_button':{
            'en': 'Select a language below',
            'fr': 'Choisissez une langue ci-dessous'
        }
    },
    'data': {
        'welcome': {
            'en': 'Welcome to the data page!',
            'fr': 'Bienvenue à la page des données!'
        },
        'browse_wd':{
            'en': 'Browse working directory',
            'fr': 'Parcourir le répertoire de travail'
        },
        'select_wd': {
            'en': 'Select working directory. The working directory will be used to store all files created in the data validation',
            'fr': 'Sélectionner le répertoire de travail. Cette répertoire sera utilisé pour stocker tous les fichiers créés dans la validation'
        },
        'confirm_wd': {
            'en': 'The following working directory was selected: ',
            'fr': 'Le répertoire de travail sélectionné est: '
        },
        'browse_image': {
            'en': 'Browse image directory',
            'fr': 'Parcourir le répertoire des images'
        },
        'select_image': {
            'en': 'Select image directory. This is the directroy containing all images taken by the citizen scientists, downloaded from the Kobo website.',
            'fr': 'Sélectionner le répertoire des images. Cette répertoire contient toutes les images prises par les volontaires scientifiques, téléchargées depuis le site Kobo.'
        },
        'confirm_image': {
            'en': 'The following image directory was selected: ',
            'fr': 'Le répertoire des images sélectionné est: '
        },
        'browse_kobo': {
            'en': 'Browse to the excel sheet downloaded from the Kobo Website',
            'fr': 'Parcourir le Excel sheet téléchargé depuis le site Kobo'
        },
        'select_kobo': {
            'en': 'Please select data file downloaded from Kobo. This file contains all the records that are meant to be processed.',
            'fr': 'Sélectionner le Excel sheet téléchargé depuis le site Kobo. Cette sheet contient tous les enregistrements qui doivent être traités.'
        },
        'confirm_kobo': {
            'en': 'The following Kobo sheet was selected: ',
            'fr': 'Le sheet Kobo sélectionné est: '
        },
        'browse_coordinates': {
            'en': 'Browse to the coordinates sheet',
            'fr': 'Parcourir le sheet des coordonnées'
        },
        'select_coordinates': {
            'en': 'Please select coordinates sheet. This sheet contains information and coordinates of the different villages.',
            'fr': 'Sélectionner le sheet des coordonnées. Cette sheet contient des informations et des coordonnées de différents villages.'
        },
        'confirm_coordinates': {
            'en': 'The following coordinates sheet was selected: ',
            'fr': 'Le sheet des coordonnées sélectionné est: '
        },
        'browse_previous': {
            'en': 'Select previously generated data sheet (NOT applicable if running validation for the first time)',
            'fr': 'Sélectionner le sheet précédent (NON applicable si vous exécutez une validation pour la première fois)'
        },
        'select_previous': {
            'en': "If this is the first time validating this dataset, don't select a file here. Otherwise, select the file that was created the previous time you validated the data.",
            'fr': "Si vous exécutez une validation pour la première fois, ne sélectionnez pas de fichier ici. Sinon, sélectionnez le fichier créé précédemment pour la validation.",
        },
        'confirm_previous': {
            'en': 'The following sheet was selected: ',
            'fr': 'Le sheet sélectionné est: '
        },
        'browse_settings': {
            'en': 'Select settings file',
            'fr': 'Sélectionner le fichier de paramètres'
        },
        'select_settings': {
            'en': "Please select the file containing parameters (e.g. column names, distances, scoop times etc.)",
            'fr': "Sélectionner le fichier contenant les paramètres (ex: noms des colonnes, distances, durées de serpissage etc.)"
        },
        'confirm_settings': {
            'en': 'The following file was selected: ',
            'fr': 'Le fichier sélectionné est: '
        },
        'next_page': {
            'en': "Are you ready to go to the next page?",
            'fr': 'Etes-vous prêt à aller à la page suivante?'
        },
        'back_button': {
            'en': 'Back to previous page',
            'fr': 'Retour à la page précédente'
        }
    },
    'previous': {
        'wd': {
            'en': 'Working directory: ',
            'fr': 'Repertoire de travail: '
        },
        'image': {
            'en': 'Image directory: ',
            'fr': 'Repertoire des images: '
        },
        'kobo': {
            'en': 'Kobo sheet: ',
            'fr': 'Sheet Kobo: '
        },
        'coordinates': {
            'en': 'Coordinates sheet: ',
            'fr': 'Sheet des coordonnées: '
        },
        'settings': {
            'en': 'Settings file: ',
            'fr': 'Fichier de paramètres: '
        },
        'previous': {
            'en': 'Previous sheet: ',
            'fr': 'Sheet précédent: '
        },
        'new': {
            'en': 'New sheet: ',
            'fr': 'Sheet nouveau: '
        },
        'validate_button': {
            'en': 'Start validating',
            'fr': 'Démarrer la validation'
        },
        'back_data_button': {
            'en': 'Back to data page',
            'fr': 'Retour à la page des données'
        },
        'back_start_button': {
            'en': 'Back to start page',
            'fr': 'Retour à la page de démarrage'
        }
    },
    'validation': {
        'start_validation': {
            'en': "Start new record",
            'fr': "Démarrer un nouveau enregistrement"
        },
        'missing_village': {
            'en': "The following Villages are missing in the coordinates file, no checks on the location can be done: ",
            'fr': "Les villes suivantes sont manquantes dans le fichier des coordonnées, aucun n'est pas possible de vérifier les emplacements pour ces villes: "
        },
        'adjust_village': {
             'en': 'If you want to add them or adjust the spelling, go back to the data selection page. Please adjust the names in the coordinates file, save the file and reselect.',
             'fr': 'Si vous voulez ajouter ou corriger les noms, retournez à la page de sélection des données. Veuillez corriger les noms dans le fichier coordonnées, enregistrer le fichier et recommencez la sélection des données.\n'
        },
        'button_quit': {
            'en': 'Quit',
            'fr': 'Quitter'
        },
        'button_start': {
            'en': 'Start',
            'fr': 'Démarrer'
        },
        'bio_live': {
            'en': 'Biomphalaria live snails',
            'fr': 'Biomphalaria vivants',
        },
        'bul_live': {
            'en': 'Bulinus live snails',
            'fr': 'Bulinus vivants',
        },
        'lym_live': {
            'en': 'Lymnaea live snails',
            'fr': 'Lymnaea vivants',
        },
        'pool_live': {
            'en': 'Pool live snails',
            'fr': 'Pool vivants'
        },
        'bio_empty': {
            'en': 'Biomphalaria empty shells',
            'fr': 'Biomphalaria vides', 
        },
        'bul_empty': {
            'en': 'Bulinus empty shells',
            'fr': 'Bulinus vides',
        },
        'lym_empty': {
            'en': 'Lymnaea empty shells',
            'fr': 'Lymnaea vides',
        },
        'pool_empty': {
            'en': 'Pool empty shells',
            'fr': 'Pool vides',
        },
        'error_date': {
             'en': 'Date',
             'fr': 'Date',
        },
        'error_location': {
            'en': 'Location',
            'fr': 'Emplacement'
        },
        'error_distance': {
            'en': 'Distance',
            'fr': 'Distance'
        },
        'error_scoop': {
            'en': 'Scoop time',
            'fr': 'Temps de scoop',
        },
        'error_images': {
            'en': 'Images',
            'fr': 'Images'
        },
        'error_bio_live_images': {
            'en': 'Biomphalaria live images',
            'fr': 'Biomphalaria vivants images'
        },
        'error_bul_live_images': {
            'en': 'Bulinus live images',
            'fr': 'Bulinus vivants images'
        },
        'error_lym_live_images': {
            'en': 'Lymnaea live images',
            'fr': 'Lymnaea vivants images'
        },
        'error_pool_live_images': {
            'en': 'Pool live images',
            'fr': 'Pool vivants images'
        },
        'error_bio_empty_images': {
            'en': 'Biomphalaria empty images',
            'fr': 'Biomphalaria vides images'
        },
        'error_bul_empty_images': {
            'en': 'Bulinus empty images',
            'fr': 'Bulinus vides images'
        },
        'error_lym_empty_images': {
            'en': 'Lymnaea empty images',
            'fr': 'Lymnaea vides images'
        },
        'error_pool_empty_images': {
            'en': 'Pool empty images',
            'fr': 'Pool vides images'
        },
        'error_composite_live_image': {
            'en': 'Composite live image',
            'fr': 'Image composite vivante'
        },
        'error_composite_empty_image': {
            'en': 'Composite empty image',
            'fr': 'Image composite vide'
        },
        'error_counting': {
            'en': 'Counting (correct identification)',
            'fr': 'Comptagne (identification correcte)',
        },
        'error_liveempty': {
            'en': 'Live snails vs empty shells',
            'fr': 'Vides vs vivants escargots',
        },
        'error_identification': {
            'en': 'Identification',
            'fr': 'Identification'
        },
        'error_bio': {
            'en': 'Biomphalaria identification',
            'fr': 'Biomphalaria identification'
        },
        'error_bul': {
            'en': 'Bulinus identification',
            'fr': 'Bulinus identification',
        },
        'error_lym': {
            'en': 'Lymnaea identification',
            'fr': 'Lymnaea identification',
        },
        'error_pool': {
            'en': 'Pool identification',
            'fr': 'Pool identification'
        },
        'warning_date_realistic': {
            'en': 'Error: Date is not realistic',
            'fr': 'Erreur : Date non réaliste',
        },
        'warning_date_format': {
            'en': 'Error: Date format is not correct',
            'fr': 'Erreur: Format de date incorrect',
        },
        'warning_location': {
            'en': 'Error: Location is not in coordinates data or incorrect',
            'fr': 'Erreur: Location non dans les données de coordonnées ou incorrect',
        },
        'warning_distance': {
            'en': 'Error: Sample carried out too far from village center',
            'fr': 'Erreur: Scoop location trop loin du centre de la ville'
        },
        'warning_scoop': {
            'en': 'Error: Scoop time is not within the expected range',
            'fr': "Erreur: Temps de scoop non dans l'intervalle attendu",
        },
        'no_snails_warning': {
            'en': 'No snails found in this record',
            'fr': 'Aucun escargot trouvé dans ce enregistrement'
        },
        'no_image_warning': {
            'en': 'Error: One or more images are missing in this record',
            'fr': 'Erreur : une ou plusieurs images sont manquantes dans ce enregistrement'
        },
        'warning_liveempty': {
            'en': 'Error - an empty shell was incorrectly identified as a live snail or vice versa.',
            'fr': 'Erreur - une escargot vide est incorrectement identifié comme un escargot vivant ou vice versa.'
        },
        'warning_counting': {
            'en': 'Error - There was an error in number of (correctly identified) individuals',
            'fr': 'Erreur - une erreur dans le nombre de (correctement identifiés) individu(s) des escargots'
        },
        'warning_identification': {
            'en': 'Error - one or more individuals were identified incorrectly.',
            'fr': 'Erreur - une ou plusieurs individu(s) sont incorrectement identifiés'
        },
        'warning_species_identification': {
            'en': 'Error - one or more individuals of this species were identified incorrectly.',
            'fr': 'Erreur - une ou plusieurs individu(s) de cette espèce sont incorrectement identifiés.'
        }
    },
    'checking': {
        'image_missing_text': {
            'en': 'Error - image missing of ',
            'fr': 'Erreur - image manquante de '
        },
        'yes': {
            'en': 'Yes',
            'fr': 'Oui'
        },
        'no': {
            'en': 'No',
            'fr': 'Non'
        },
        'q1': {
            'en': 'Are all individuals on the image classified correctly as \n(live and/or empty shells of) ',
            'fr': 'Tous les individu sont-ils correctement classés comme \n(vivants et/out vides escargots de) '
        },
        'q2_empty': {
            'en': 'Are there any empty shells in the image?',
            'fr': "Y-a-t-il des vides escargots dans l'image?"
        },
        'q2_live': {
            'en': 'Are there any live snails in the image?',
            'fr': "Y-a-t-il des vivants escargots dans l'image?"
        },
        'input_empty': {
            'en': 'Enter the number of empty shells in the image',
            'fr': "Entrez le nombre d'escargots vides dans l\'image"
        },
        'input_live': {
            'en': 'Enter the number of live snails in the image',
            'fr': "Entrez le nombre d'escargots vivants dans l'image"
        },
        'original_count': {
            'en': 'The original count of ',
            'fr': 'Le nombre enregistre de ',
        },
        'correct?': {
            'en': '\n Is this correct?',
            'fr': '\n Est-ce correct?'
        },
        'submit': {
            'en': 'Submit',
            'fr': 'Soumettre'
        },
        'input_correct_number_live': {
            'en': 'Input the correct number of snails in the image',
            'fr': 'Entrez le nombre correct de escargots vivants dans l\'image'
        },
        'input_correct_number_empty': {
            'en': 'Input the correct number of shells in the image',
            'fr': 'Entrez le nombre correct de escargots vides dans l\'image'
        },
        'adjust_live': {
            'en': 'Adjust values of live snails if necessary',
            'fr': 'Ajustez les valeurs des escargots vivants si nécessaire.'
        },
        'adjust_empty': {
            'en': 'Adjust values of empty shells if necessary',
            'fr': 'Ajustez les valeurs des escargots vides si nécessaire.'
        },
        'live_missing': {
            'en': 'Composite image of live snails missing',
            'fr': 'Image des escargots vivants manquante'
        },
        'empty_missing': {
            'en': 'Composite image image of empty shells missing',
            'fr': 'Image des escargots vides manquante'
        },
        'record_finished': {
            'en': 'Record finished',
            'fr': 'Enregistrement terminé'
        },
        'quit_save': {
            'en': 'Quit and save',
            'fr': 'Quitter et enregistrer'
        }
    }
}

class LanguageDialog(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Select Language")
        self.geometry("300x150")

        # Label
        label = tk.Label(self, text="Please choose a language:")
        label.pack(pady=10)

        # Buttons for language selection
        english_button = tk.Button(self, text="English", command=lambda: self.select_language("en"))
        english_button.pack(pady=5)

        french_button = tk.Button(self, text="French", command=lambda: self.select_language("fr"))
        french_button.pack(pady=5)

        # Center the dialog on the screen
        self.grab_set()
        self.wait_window(self)

    def select_language(self, lang):
        self.controller.language = lang
        self.controller.lang_dict = dictionary
        self.destroy()

class CS_gui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initial configuration
        self.geometry('600x600')
        self.title('Snail validation - GUI')

        self.frames = {}
        self.language = 'fr'  # Default language
        self.lang_dict = dictionary

        # Show the language selection dialog before creating the main application
        self.show_language_dialog()

    def get_lang_dict_for_language(self, lang):
        # Replace this with your actual logic to get the language dictionary
        return dictionary if lang == 'fr' else dictionary

    def show_language_dialog(self):
        # Show the language selection dialog
        dialog = LanguageDialog(self, self)

        # Initialize StartPage after selecting the language
        # Ensure that the language is set before creating StartPage
        self.after(100, self.create_start_page)

    def create_start_page(self):
        if not hasattr(self, 'start_page') or self.start_page is None:
            self.start_page = StartPage(parent=self, controller=self)
            self.start_page.grid(row=0, column=0, sticky="nsew")

        # Show StartPage
        self.show_frame("StartPage")

    def create_pages(self):
        # Create pages when the start button is pressed
        for F in (DataDescriptionPage, PreviousPage, ValidationPage):
            page_name = F.__name__
            if page_name not in self.frames:
                print(f"Creating page: {page_name}")  # Debug print
                frame = F(parent=self, controller=self)
                if frame is None:
                    print(f"Failed to create {page_name}")  # Debug print
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")

        # Show the DataDescriptionPage by default after creation
        self.show_frame("DataDescriptionPage")

    def update_all_frames(self, language):
        self.language = language
        self.lang_dict = dictionary
        for frame_name, frame in self.frames.items():
            if frame is None:
                print(f"Frame '{frame_name}' is None")  # Debug print
                continue
            if hasattr(frame, 'update_values_langdict'):
                lang_dict = self.lang_dict
                frame.update_values_langdict(self.language, lang_dict)
            elif hasattr(frame, 'update_labels') and frame_name in ['PreviousPage', 'ValidationPage']:
                data_page = self.frames.get("DataDescriptionPage")
                if data_page is None:
                    print("DataDescriptionPage is None")  # Debug print
                if data_page:
                    wd = data_page.get_wd()
                    image = data_page.get_image()
                    kobo = data_page.get_kobo()
                    coordinates = data_page.get_coordinates()
                    previous = data_page.get_previous()
                    new = data_page.get_new()
                    settings = data_page.get_settings()
                    frame.update_labels(wd, image, kobo, coordinates, previous, new, settings)
            elif hasattr(frame, 'update_values') and frame_name == 'ValidationPage':
                data_page = self.frames.get("DataDescriptionPage")
                if data_page is None:
                    print("DataDescriptionPage is None")  # Debug print
                if data_page:
                    wd = data_page.get_wd()
                    image = data_page.get_image()
                    kobo = data_page.get_kobo()
                    coordinates = data_page.get_coordinates()
                    previous = data_page.get_previous()
                    new = data_page.get_new()
                    name = data_page.get_name()
                    date = data_page.get_date()
                    settings = data_page.get_settings()
                    frame.update_values(wd, image, kobo, coordinates, previous, new,name,date,settings)
                    frame.process_data()
            frame.tkraise()

    def show_frame(self, page_name):
        print(f"Showing frame: {page_name}")  # Debug print

        if page_name == "StartPage":
            frame = self.start_page
        else:
            if page_name not in self.frames:
                print(f"Page '{page_name}' not in frames. Creating pages...")  # Debug print
                self.create_pages()

            frame = self.frames.get(page_name)
        
        if frame is None:
            print(f"Frame '{page_name}' is None")  # Debug print
            return

        if page_name in ['DataDescriptionPage', 'PreviousPage', 'ValidationPage']:
            if page_name != "StartPage":
                data = self.start_page
                lang = data.get_language()
                dict = self.get_lang_dict_for_language(lang)
                frame.update_values_langdict(lang, dict)

        if page_name == "PreviousPage":
            data_page = self.frames.get("DataDescriptionPage")
            if data_page:
                wd = data_page.get_wd()
                image = data_page.get_image()
                kobo = data_page.get_kobo()
                coordinates = data_page.get_coordinates()
                previous = data_page.get_previous()
                new = data_page.get_new()
                settings = data_page.get_settings()
                frame.update_labels(wd, image, kobo, coordinates, previous, new, settings)

        if page_name == "ValidationPage":
            data_page = self.frames.get("DataDescriptionPage")
            if data_page:
                wd = data_page.get_wd()
                image = data_page.get_image()
                kobo = data_page.get_kobo()
                coordinates = data_page.get_coordinates()
                previous = data_page.get_previous()
                new = data_page.get_new()
                name = data_page.get_name()
                date = data_page.get_date()
                settings = data_page.get_settings()
                frame.update_values(wd, image, kobo, coordinates, previous, new,name,date,settings)
                frame.process_data()

        frame.tkraise()

# Instantiate the GUI
if __name__ == "__main__":
    app = CS_gui()
    app.mainloop()