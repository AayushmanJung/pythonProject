from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text = "Tkinter program beggining")
myLabel2 = Label(root, text = "I am Aayushman")
myLabel3 = Label(root, text = "HELLO YOUR COMPUTER HAS VIRUS")

#Shoving it onto the screen based upon x-axis and y-axis
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)
myLabel3.grid(row=1,column=5)

root.mainloop()