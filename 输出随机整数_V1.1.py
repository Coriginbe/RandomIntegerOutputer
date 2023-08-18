from tkinter import *
from tkinter import font
from tkinter.messagebox import *
import random

def judge():
    num1=input1.get()
    num2=input2.get()
    if num1.isdigit() and num2.isdigit() and num1<=num2:
        var.set(random.randint(int(num1),int(num2)))
    elif num1>num2:
        showinfo('Info','ValueError: empty range for randrange()')
    else:
        showinfo('Info','SyntaxError: invalid character')

root=Tk()
root.title('输出随机整数 V1.1')
root.geometry('540x540')

Label(root,text='起始数：',font=('NSimSun',15)).place(relx=0.1,rely=-0.32,relheight=0.9,relwidth=0.15)
input1=Entry(root,font=('NSimSun',15))
input1.place(relx=0.225,rely=0.1, relheight=0.05,relwidth=0.1)

Label(root,text='结束数：',font=('NSimSun',15)).place(relx=0.6,rely=-0.32,relheight=0.9,relwidth=0.15)
input2=Entry(root,font=('NSimSun',15))
input2.place(relx=0.725,rely=0.1, relheight=0.05,relwidth=0.1)

var=StringVar()
Entry(root,textvariable=var,font=('NSimSun',30)).place(relx=0.4,rely=0.4,relheight=0.2,relwidth=0.2)
Button(root,text='输出',font=('NSimSun',15),command=judge).place(relx=0.4,rely=0.6,relheight=0.1,relwidth=0.2)

root.mainloop()