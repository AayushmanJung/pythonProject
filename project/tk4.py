from tkinter import *

root=Tk()

#Button without any functions
myButton = Button(root,text="Don't Press")
myButton.pack()

myButton1 = Button(root, text="Press",state=DISABLED)
myButton1.pack()

myButton2 = Button(root, text="Enter", padx=50)
myButton2.pack()
myButton3 = Button(root, text="Enter", padx=50,pady=50)
myButton3.pack()

root.mainloop()