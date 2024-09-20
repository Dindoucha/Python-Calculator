from tkinter import *
from tkinter.font import Font
cal = Tk()
cal.geometry("325x365")
cal.resizable(False, False)
cal.title("Calculator By Dindoucha")
num = StringVar()
nums=""
myFont = Font(family="Arial", size=20)
calScreen = Entry(cal , font=myFont,textvariable = num ).place(height=40 , width = 400)

def onclick(x):
    global nums
    nums = nums +str(x)
    num.set(nums)
def clear():
    global nums
    num.set("")
    nums=""
def Eval():
    global nums
    total = eval(nums)
    nums = str(total)
    num.set(total)
h = 75
w = 75
x1=5
x2=10+w
x3=15+2*w
x4=20+3*w
y1=45
y2=50+h
y3=55+2*h
y4=60+3*h
add = Button(cal, text=" + ",font=myFont, command=lambda:onclick("+")).place(height = h , width = w , x =x4, y = y4)
minus = Button(cal, text=" - ",font=myFont,command=lambda:onclick("-")).place(height = h , width = w, x =x4, y = y3)
div = Button(cal,text=" / ",font=myFont,command=lambda:onclick("/")).place(height = h , width = w , x =x4, y =y2)
mult = Button(cal,text=" x ",font=myFont,command=lambda:onclick("*")).place(height = h , width = w, y =y1 , x =x4)
equal = Button(cal,text=" = " , font=myFont,command=lambda :Eval()).place(height = h , width = w ,x = x3, y = y4)
clr = Button(cal, text="clear" , font=myFont,command=lambda :clear()).place(height = h , width = w,x=x2, y = y4)
n0 = Button(cal , text=" 0 ", font=myFont,command =lambda:onclick("0")).place(height = h , width = w,x=x1, y = y4)
n1 = Button(cal, text=" 1 ", font=myFont,command =lambda:onclick("1")).place(height = h , width = w,x=x1, y = y3)
n2 = Button(cal, text=" 2 ", font=myFont,command =lambda:onclick("2")).place(height = h , width = w,x=x2, y = y3)
n3 = Button(cal, text=" 3 ",font=myFont, command =lambda:onclick("3")).place(height = h , width = w ,x = x3 , y = y3)
n4 = Button(cal, text=" 4 ",font=myFont, command =lambda:onclick("4")).place(height = h , width = w,x=x1, y =y2)
n5 = Button(cal, text=" 5 ",font=myFont, command =lambda:onclick("5")).place(height = h , width = w,x=x2, y =y2)
n6 = Button(cal, text=" 6 ",font=myFont, command =lambda:onclick("6")).place(height = h , width = w ,x = x3, y =y2)
n7 = Button(cal, text=" 7 ", font=myFont,command =lambda:onclick("7")).place(height = h , width = w,y=y1,x=x1)
n8 = Button(cal, text=" 8 ", font=myFont,command =lambda:onclick("8")).place(height = h , width = w,y=y1,x=x2)
n9 = Button(cal, text=" 9 ",font=myFont, command =lambda:onclick("9")).place(height = h , width = w,y=y1 ,x = x3)

cal.mainloop()