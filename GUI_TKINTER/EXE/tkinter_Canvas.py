from tkinter import *
from tkinter import messagebox
top = Tk()  
  
top.geometry("2000x2000")  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink",height = "2000",width = "2000")  
arc=c.create_arc((5,1000,150,2000),start = 0,extent = 100, fill= "white")
  
c.pack()  
  
top.mainloop()