from tkinter import *
import tkinter as tk
from tkinter import ttk
from math import *
b1=0
b2=0
def cl_e1():
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def ins_txt0():
    global a0
    a0=btn0.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a0)
    e1.config(state='readonly')
    
def ins_txt1():
    global a1
    a1=btn1.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a1)
    e1.config(state='readonly')
    
def ins_txt2():
    global a2
    a2=btn2.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a2)
    e1.config(state='readonly')
 
def ins_txt3():
    global a3
    a3=btn3.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a3)
    e1.config(state='readonly')
    
def ins_txt4():
    global a4
    a4=btn4.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a4)
    e1.config(state='readonly')
    
def ins_txt5():
    global a5
    a5=btn5.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a5)
    e1.config(state='readonly')
    
def ins_txt6():
    global a6
    a6=btn6.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a6)
    e1.config(state='readonly')
    
def ins_txt7():
    global a7
    a7=btn7.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a7)
    e1.config(state='readonly')
def ins_txt8():
    global a8
    a8=btn8.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a8)
    e1.config(state='readonly')
def ins_txt9():
    global a9
    a9=btn9.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a9)
    e1.config(state='readonly')
def g_en0():
    global ac1,b1
    ac1='+'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en1():
    global ac1,b1
    ac1='-'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en2():
    global ac1,b1
    ac1='*'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en3():
    global ac1,b1
    ac1='/'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en5():
    global ac1,b1
    ac1='^'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en6():
    global ac1,b1
    ac1='^1/n'
    b1=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    e1.config(state='readonly')
def g_en4():
    global b1,b2,rez
    b2=float(e1.get())
    e1.config(state='normal')
    e1.delete(0,'end')
    if ac1=='+':
        rez=b1+b2
        rez=str(rez)
        e1.insert(tk.END,rez)
    if ac1=='-':
        rez=b1-b2
        rez=str(rez)
        e1.insert(tk.END,rez)
    if ac1=='*':
        rez=b1*b2
        rez=str(rez)
        e1.insert(tk.END,rez)
    if ac1=='/':
        rez=b1/b2
        rez=str(rez)
        e1.insert(tk.END,rez)
    if ac1=='^':
        rez=b1**b2
        rez=str(rez)
        e1.insert(tk.END,rez)
    if ac1=='^1/n':
        if b2%2== 0 and b1<0 or b1==0 and b2==0:
            e1.insert(tk.END,"error")
        else:
            rez=b1**(1/b2)
            rez=str(rez)
            e1.insert(tk.END,rez)
    
    e1.config(state='readonly')

def dot():
    global a1
    a1=btn16.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END,a1)
    e1.config(state='readonly')
ml=tk.Tk()
ml.title("Pieteikums")
ml.geometry("300x400")
btn0=tk.Button(ml,text="0",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt0)
btn0.place(x=95, y=320,width= 50,height=50,)
btn1=tk.Button(ml,text="1",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt1)
btn1.place(x=45, y= 270,width= 50,height=50,)
btn2=tk.Button(ml,text="2",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt2)
btn2.place(x=95, y= 270,width= 50,height=50,)
btn3=tk.Button(ml,text="3",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt3)
btn3.place(x=145, y= 270,width= 50,height=50,)
btn4=tk.Button(ml,text="4",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt4)
btn4.place(x=45, y= 220,width= 50,height=50,)
btn5=tk.Button(ml,text="5",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt5)
btn5.place(x=95, y= 220,width= 50,height=50,)
btn6=tk.Button(ml,text="6",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt6)
btn6.place(x=145, y= 220,width= 50,height=50,)
btn7=tk.Button(ml,text="7",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt7)
btn7.place(x=45, y= 170,width= 50,height=50,)
btn8=tk.Button(ml,text="8",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt8)
btn8.place(x=95, y= 170,width= 50,height=50,)
btn9=tk.Button(ml,text="9",bg='grey',fg='white',font=('arial ',14,'bold'),command=ins_txt9)
btn9.place(x=145, y= 170,width= 50,height=50,)
btn10=tk.Button(ml,text="+",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en0)
btn10.place(x=195, y= 170,width= 50,height=50,)
btn11=tk.Button(ml,text="-",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en1)
btn11.place(x=195, y= 220,width= 50,height=50,)
btn12=tk.Button(ml,text="/",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en3)
btn12.place(x=195, y= 270,width= 50,height=50,)
btn13=tk.Button(ml,text="*",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en2)
btn13.place(x=195, y= 320,width= 50,height=50,)
btn14=tk.Button(ml,text="=",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en4)
btn14.place(x=145, y= 320,width= 50,height=50,)
btn17=tk.Button(ml,text="x^n",bg='grey',fg='white',font=('arial ',14,'bold'),command=g_en5)
btn17.place(x=95, y= 120,width= 50,height=50,)
btn18=tk.Button(ml,text="x^(1/n)",bg='grey',fg='white',font=('arial ',10,'bold'),command=g_en6)
btn18.place(x=145, y= 120,width= 50,height=50,)
btn15=tk.Button(ml,text="C",bg='grey',fg='white',font=('arial ',14,'bold'),command=cl_e1)
btn15.place(x=45, y= 120,width= 50,height=50,)
btn16=tk.Button(ml,text=".",bg='grey',fg='white',font=('arial ',14,'bold'),command=dot)
btn16.place(x=45, y= 320,width= 50,height=50,)
e1=ttk.Entry()
e1.place(x=46,y=60,width= 200,height=20)
e1.config(state='readonly')

ml.mainloop()