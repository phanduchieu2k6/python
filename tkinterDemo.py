from tkinter import *
import math

tk=Tk()
sa=StringVar()
sb=StringVar()
sc=StringVar()
kq=StringVar()
def reset():
    sa.set("")
    sb.set("")
    sc.set("")
    kq.set("")
def giai():
    a=float(sa.get())
    b=float(sb.get())
    c=float(sc.get())
    d=b**2-4*a*c
    if d<0:
        kq.set("Vo nghiem")
    elif d==0:
        kq.set("x="+str(-b/(2*a)))
    elif d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        kq.set("x1="+str(x1)+" "+"x2="+str(x2))
Label(tk,text="tinh phuong trinh bac hai: ax^2+bx+c=0",fg="red").pack()
Label(tk,text="a: ").pack()
Entry(tk,textvariable=sa).pack()
Label(tk,text="b: ").pack()
Entry(tk,textvariable=sb).pack()
Label(tk,text="c: ").pack()
Entry(tk,textvariable=sc).pack()
Button(tk,text="Giai",command=giai).pack()
Button(tk,text="Reset",command=reset).pack()
Button(tk,text="Quit",command=tk.quit).pack()
Label(tk,text="Ket qua: ").pack()
Entry(tk,textvariable=kq).pack()
tk.mainloop()