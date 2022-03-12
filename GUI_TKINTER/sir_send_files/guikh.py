# GUI
# tkinter
#import tkinter
#from tkinter import*
'''
from tkinter import*
root=Tk()
root.title('my window')
root.geometry('400x300')
root.mainloop()

# font
from tkinter import*
from tkinter import font
root=Tk()

list_font=list(font.families())
print(list_font)

# color blue, black

# containers
# canvas   ,   frame


# c=Canvas(root,bg='blue',height=500,width=600,cursor='pencil')
# c.pack()
'''
from tkinter import*
root=Tk()
root.title('my window')
c=Canvas(root,bg='blue',height=500,width=600,cursor='plus')
c.pack()
#c.create_rectangle(50,100,200,300,width=2,fill='gray',activefill='yellow')
#c.create_line(50,50,200,50,200,400,50,400,50,50,width=5)
fnt=('Times',40,'bold italic underline')
#c.create_text(200,200, text='MY CANVAS', font=fnt,fill='yellow')
c.create_polygon(10,10,200,200,300,200, width=3,fill='green',
                 activefill='white')
#c.create_oval(100,100,400,300, width=3, fill='yellow', outline='red')


# c.create_rectangle(500,200,700,600,width=2,fill='gray')


# cursor
# arrow, cross, mouse, pencil, plus, star, umbrella, watch

# arc

c.create_arc(500,100,300,400, width=3,start=90,extent=180,
             outline='red',style='arc')

root.mainloop()



     







