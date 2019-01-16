from tkinter import *
from tkinter import messagebox
a = Tk()
def sel():
    i = C3.get()
    s = "You have selected the option: "+str(i)
    label.config(text=s)
def check1():
    a = CheckVar1.get()
    if a==1:
        webbrowser.open("news.google.com")
    else:
        print("Music Off")
def check2():
    a = CheckVar2.get()
    if a ==1:
        webbrowser.open("news.yahoo.com")
    else:
        print("Video Off")
C3 = IntVar()   
R1 = Radiobutton(a,text="Music",variable=C3,value = 1,command = sel)
R2 = Radiobutton(a,text="Video",variable=C3,value = 2,command = sel)
R3 = Radiobutton(a,text="Image",variable=C3,value = 3,command = sel)
label = Label(a,text="Select an option")
label.pack()
R1.pack()
R2.pack()
R3.pack()
# a.geometry("500x500+0+0")
filename = PhotoImage(file = "C:\\Users\\dell\\Itronix\\12.png")
background_label = Label(a, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()
a.title("Hello World")
CheckVar1 = IntVar()
CheckVar2 = IntVar()

 
# C1 =  Checkbutton(a,text = "Music",variable = CheckVar1,onvalue = 1,offvalue=0,command=check1)
# C2 =  Checkbutton(a,text = "Video",variable = CheckVar2,onvalue = 1,offvalue=0,command=check2)


# C1.pack()
# C2.pack()

a.mainloop()
