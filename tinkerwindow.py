# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import webview
from tkinter import ttk



#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x270")

def open_popup():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Child Window")
   Label(win, text= "i'm listening.", font=('Helvetica 33 bold')).place(x=120,y=80)

Label(win, text=" Click the Button to speak", font = ('Helvetica 23 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Open", command= open_popup).pack()
win.mainloop()

label = Label(master,
			text ="welcome, I'm listening.")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
# btn = Button(master,
# 			text ="Click to open a new window",
# 			command = openNewWindow)

# btn.pack(pady = 10)

# mainloop, runs infinitely
#mainloop()

