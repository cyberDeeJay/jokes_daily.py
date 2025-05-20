import tkinter as tk
from tkinter import *
import pyjokes

# Create the main window
root = tk.Tk()
root.geometry('619x565')
root.title("Jokes Daily")

#this is to change window color, google hex color picker, select color,copy and paste hex here
root.config(background='#3c1da1')

#image logo on the top window. does not recognize line 14, revize and debug
photo = PhotoImage(file='yaoming.png')
#root.iconphoto(True, laughing_guy)

joke='want a joke?'

#function for our button
def give_joke():
	label.config(text=(pyjokes.get_joke())) 


# Create a button widget
button = tk.Button(root, text="Click for Joke!",
	font=('Arial',32,'bold'),
	fg='#e3b41b',
	bg='purple',
	relief=RAISED,
	bd=10,
	activebackground='gold')

# Add a label to the window										        
label = tk.Label(root, 
	text="Want to hear something funny?!",
	font=('Arial',40,'bold'),
	fg='#e3b41b',	#fg=fore ground
	bg='purple',	#bg=background
	relief=RAISED,
	bd=10,	#border
	padx=20,	#padding sides the text
	pady=20,
	image=photo)
label.pack()

#this will print out the answer for give_joke
label=Label(root,text=give_joke)
label.config(font=('Arial',20))
label.pack()

#this action allows you to link a funtion to the button.
#print(pyjokes.get_joke())  function to get jokes from pyjokes
button.config(command=give_joke)

button.pack()

# Start the Tkinter event loop
root.mainloop()
