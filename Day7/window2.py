from tkinter import *
i=0
def func1():
    global a1
    a.destroy()
    a1=Tk()
    a1.geometry("500x500+30+30")
    w1=Button(a1,text="Page 2",bg="white",fg="black",width=10,height=5,bd=5,command=home)
    w1.pack()
    a1.mainloop()
    
def home():
    global i
    i=i+1
    if i>1:
        a1.destroy()
    global a
    a=Tk()
    a.geometry("500x500+30+30") 
    w=Button(a,text="Page 1",bg="white",fg="black",width=10,height=5,bd=5,command=func1)
    w.pack()
    a.mainloop()

home()
