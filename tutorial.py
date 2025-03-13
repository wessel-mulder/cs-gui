import tkinter as tk 

root = tk.Tk()

# Window
root.geometry('500x500')
root.title('Snail Validation')

# Label
label = tk.Label(root, text= "Welcome to the snail detector!",
                 font=('Arial', 18))
label.pack(padx=20,pady=20)

# Textbox
textbox = tk.Text(root,height =3, font =('Arial', 16))
textbox.pack()

# Entry
myentry = tk.Entry(root)
myentry.pack()

#Button
button = tk.Button(root, text = 'Click Me!', font = ('Arial',18))
button.pack()

# Buttonframe 
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe,text ='1', font = ('Arial', 10))
btn1.grid(row=0,column=0,sticky = tk.W+tk.E)
btn2 = tk.Button(buttonframe,text ='2', font = ('Arial', 10))
btn2.grid(row=0,column=1,sticky = tk.W+tk.E)
btn3 = tk.Button(buttonframe,text ='3', font = ('Arial', 10))
btn3.grid(row=0,column=2,sticky = tk.W+tk.E)
btn4 = tk.Button(buttonframe,text ='4', font = ('Arial', 10))
btn4.grid(row=1,column=0,sticky = tk.W+tk.E)
btn5 = tk.Button(buttonframe,text ='5', font = ('Arial', 10))
btn5.grid(row=1,column=1,sticky = tk.W+tk.E)
btn6 = tk.Button(buttonframe,text ='6', font = ('Arial', 10))
btn6.grid(row=1,column=2,sticky = tk.W+tk.E)

buttonframe.pack(fill = 'x')

anotherbtn = tk.Button(root, text = 'TEST')
anotherbtn.place(x = 200,y = 400, height = 100, width = 100)
# Main loop
root.mainloop()