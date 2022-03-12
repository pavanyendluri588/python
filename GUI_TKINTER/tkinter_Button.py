from tkinter import *
from tkinter import messagebox
"""
The button widget is used to add various types of buttons to the python application. 
Python allows us to configure the look of the button according to our requirements.
 Various options can be set or reset depending upon the requirements.

We can also associate a method or function with a button which is called when the button is pressed.


"""

root=Tk()
root.geometry("200x100")  

def function():
        messagebox.showinfo("successfully function is activated by the function")
button1=Button(root,text="button1",activebackground="red",activeforeground="yellow",Command=function(),pady=10)
button2=Button(root,text="button1",pady=10).place(x=20,y=80)
button3=Button(root,text="button1",pady=10).place(x=180,y=80)
button4=Button(root,text="button1",pady=10).place(x=100,y=140)
button1=pack(side=LEFT)
button2=pack(side=TOP)
button3=pack(side=BOTTOM)
button4=pack(side=RIGHT)
root.mainloop()
"""
Font
Height
heighlightcolor
image
justify
padx
pady

missing attributes:
Relif
state
underline
width
wraplength

"""