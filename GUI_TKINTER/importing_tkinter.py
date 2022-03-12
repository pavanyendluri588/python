from tkinter import  *
boox_module=Tk()
username=Label(boox_module,text="USERNAME",fg="red",bg="yellow").place(x=30,y=30)
password=Label(boox_module,text="PASSWORD",fg="green").place(x=30,y=50)
input_username=Entry(boox_module).place(x=100,y=30)
input_password=Entry(boox_module).place(x=100,y=50  )
#button
submit=Button(boox_module,text="submit").place(x=90,y=70)
if submit==True:
    username=None
    password=None

boox_module.mainloop()
