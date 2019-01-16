## TKINTER GUI

from tkinter import *
from tkinter import messagebox

def fun1():
	messagebox.showinfo("Say Hello","Hello World")
a = Tk()
a.title("Shopping")
a.geometry("500x500+100+100")
B1 = Button(a,text= "     ",height = 10,width=5)
B2 = Button(a,text = "Average",height=5,width=11)
B3 = Button(a,text = "Height",height=5,width=5)
B4 = Button(a,text= "Weight",height=5,width=5)
B5 = Button(a,text = "Red Eyes",height=10,width=5)
B6 = Button(a,text = "Males")
B7 = Button(a,text= "Females")
B8 = Button(a,text = "1.9")
B9 = Button(a,text = "1.7")
B10 = Button(a,text = "0.03")
b11 = Button(a,text= "0.002")
b12= Button(a,text="40%")
b13 = Button(a,text="43%")
B1.grid(row= 0,column = 0,rowspan =2,columnspan= 1)
B2.grid(row = 0,column = 1,rowspan = 1,columnspan =2)
B5.grid(row=0,column = 3,rowspan=2,columnspan=1)
B3.grid(row=1,column = 1,rowspan=1,columnspan=1)
B4.grid(row=1,column=2,rowspan=1,columnspan=1)

a.mainloop()