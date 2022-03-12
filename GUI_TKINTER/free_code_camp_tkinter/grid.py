from tkinter  import *
#from tkinter import 
root=Tk()# thiis is the first step to do while working with the tkinter
label1=Label(root,text="Hello world!")
label2=Label(root,text="My name is yendluri pavan ram chandar")
label1.grid(row=1,column=1)
label2.grid(row=2,column=1)

#label1.pack()

root.mainloop()