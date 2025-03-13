The 'main' part of the code operates through _main.py_. This code initiates the first window and the different 'pages' users
scroll through as they move through the program. This also contains the code required to transer information between these pages
and ensure information is 'up to date' as the new pages are called. 

pages/ contains the different pages users scroll through. these contain most of the functionality that each pages is 
required to do. If I remember correctly, the pages go from start > data > previous > validation > checking. In checking, 
the different questions lead to different responses/pop-ups based on the answers being given (with the button).

There are some support functions in aesthetics/, I included all other code I found in the working directory just in case, but I'm not sure if any of them are support functions that are actually used - I didn't want to mess with the folder structure so that's why they're all loose like this. 

The app is built using TKinter functionalities, and converted to a standalone exec using PyInstaller. 



