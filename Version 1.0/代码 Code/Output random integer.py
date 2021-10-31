from tkinter import *
from tkinter import font
from tkinter.messagebox import *
import random

def judge():
    num1=input1.get()
    num2=input2.get()
    if num1.isdigit() and num2.isdigit():
        var.set(random.randint(int(num1),int(num2)))
    else:
        showinfo('Information','Invalid character.')

root=Tk()
root.title('Output random integer')
root.geometry('540x540')

Label(root,text='Starting interger:',font=('NSimSun',15)).place(relx=0.02,rely=-0.32,relheight=0.9,relwidth=0.35)
input1=Entry(root,font=('NSimSun',15))
input1.place(relx=0.36,rely=0.1, relheight=0.05,relwidth=0.1)

Label(root,text='Ending interger:',font=('NSimSun',15)).place(relx=0.52,rely=-0.32,relheight=0.9,relwidth=0.3)
input2=Entry(root,font=('NSimSun',15))
input2.place(relx=0.815,rely=0.1, relheight=0.05,relwidth=0.1)

var=StringVar()
Entry(root,textvariable=var,font=('NSimSun',30)).place(relx=0.4,rely=0.4,relheight=0.2,relwidth=0.2)
Button(root,text='Output',font=('NSimSun',15),command=judge).place(relx=0.4,rely=0.6,relheight=0.1,relwidth=0.2)

root.mainloop()