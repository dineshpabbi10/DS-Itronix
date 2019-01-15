from tkinter import *
from tkinter import messagebox

a=Tk()
a.title("Shopping Cart")
a.geometry("500x500+0+0")

def fun1():
    messagebox.showinfo("Hello Python","Hello World")


B1=Button(a,text="Button1",width=15,height=5,bd=5,fg="blue",bg="yellow",command=fun1,relief=FLAT)
B2=Button(a,text="Button2",width=15,height=5,bd=5,fg="blue",bg="white",command=fun1,relief=RAISED)
B3=Button(a,text="Button3",width=15,height=5,bd=5,fg="white",bg="black",command=fun1,relief=SUNKEN)
B4=Button(a,text="Button4",width=15,height=5,bd=5,fg="white",bg="black",command=fun1,relief=GROOVE)
B5=Button(a,text="Button5",width=15,height=5,bd=5,fg="blue",bg="red",command=fun1,relief=RIDGE)
B1.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30)
B2.pack(side=TOP)
B3.pack(side=TOP)
B4.pack(side=TOP)
B5.pack(side=TOP,expand=0)

a.mainloop()
