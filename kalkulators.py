from tkinter import *
import tkinter as tk
from tkinter import ttk
from math import *

# Initialize global variables for calculation logic
b1 = 0          # First operand
b2 = 0          # Second operand
global ac1
ac1 = '0'       # Stores the current arithmetic operator

def cl_e1():
    """Clears the entry field and resets it to '0'."""
    global b1
    e1.config(state='normal')       # Enable widget to modify text
    e1.delete(0, 'end')             # Clear all text
    e1.insert(tk.END, '0')          # Reset to default zero
    e1.config(state='readonly')     # Set back to read-only for user safety

def ins_txt0():
    """Fetches the text from button 0 and inserts it into the entry field."""
    global a0
    a0 = btn0.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a0)
    e1.config(state='readonly')

# Functions ins_txt1 through ins_txt9 follow the same logic as ins_txt0
def ins_txt1():
    global a1
    a1 = btn1.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a1)
    e1.config(state='readonly')

def ins_txt2():
    global a2
    a2 = btn2.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a2)
    e1.config(state='readonly')

def ins_txt3():
    global a3
    a3 = btn3.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a3)
    e1.config(state='readonly')

def ins_txt4():
    global a4
    a4 = btn4.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a4)
    e1.config(state='readonly')

def ins_txt5():
    global a5
    a5 = btn5.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a5)
    e1.config(state='readonly')

def ins_txt6():
    global a6
    a6 = btn6.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a6)
    e1.config(state='readonly')

def ins_txt7():
    global a7
    a7 = btn7.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a7)
    e1.config(state='readonly')

def ins_txt8():
    global a8
    a8 = btn8.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a8)
    e1.config(state='readonly')

def ins_txt9():
    global a9
    a9 = btn9.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a9)
    e1.config(state='readonly')

def g_en0():
    """Sets addition operator and stores the first number."""
    global ac1, b1
    ac1 = '+'
    b1 = float(e1.get())
    e1.config(state='normal')
    e1.delete(0, 'end')
    e1.config(state='readonly')

def g_en1():
    """Handles subtraction or negative number input logic."""
    global ac1, b1, c
    ac1 = '-'
    c = e1.get()
    if not c:  # If entry is empty, treat '-' as a sign, not an operator
        e1.config(state='normal')
        e1.insert(tk.END, ac1)
        e1.config(state='readonly')
        ac1 = '0'
    else:      # Otherwise, treat as subtraction operator
        b1 = float(e1.get())
        e1.config(state='normal')
        e1.delete(0, 'end')
        e1.config(state='readonly')

def g_en2():
    """Sets multiplication operator and stores the first number."""
    global ac1, b1
    ac1 = '*'
    b1 = float(e1.get())
    e1.config(state='normal')
    e1.delete(0, 'end')
    e1.config(state='readonly')

def g_en3():
    """Sets division operator and stores the first number."""
    global ac1, b1
    ac1 = '/'
    b1 = float(e1.get())
    e1.config(state='normal')
    e1.delete(0, 'end')
    e1.config(state='readonly')

def g_en5():
    """Sets power/exponentiation operator."""
    global ac1, b1
    ac1 = '^'
    b1 = float(e1.get())
    e1.config(state='normal')
    e1.delete(0, 'end')
    e1.config(state='readonly')

def g_en6():
    """Instantly calculates the square root of the current number."""
    global ac1, b1
    ac1 = '^1/n'
    b1 = float(e1.get())
    e1.config(state='normal')
    e1.delete(0, 'end')
    b1 = b1**0.5  # Calculate square root
    e1.insert(tk.END, b1)
    e1.config(state='readonly')

def g_en4():
    """The 'Equal' button logic: performs the math based on stored operator."""
    global b1, b2, rez, ac1, c
    e1.config(state='normal')
    c = e1.get()
    
    if not c:
        b1 = 0
        
    if ac1 == '0':
        # If no operator selected, return current value
        b1 = float(e1.get())
        rez = float(e1.get())
    else:
        # Perform calculation based on the active operator (ac1)
        b2 = float(e1.get())
        e1.delete(0, 'end')
    
        if ac1 == '+':
            rez = b1 + b2
        elif ac1 == '-':
            rez = b1 - b2
        elif ac1 == '*':
            rez = b1 * b2
        elif ac1 == '/':
            rez = b1 / b2
        elif ac1 == '^':
            rez = b1 ** b2
            
        # Display the result
        rez = str(rez)
        e1.insert(tk.END, rez)
        b1 = float(e1.get()) # Update b1 for potential chained calculations

    e1.config(state='readonly')
    ac1 = 0 # Reset operator

def dot():
    """Inserts a decimal point."""
    global a1
    a1 = btn16.cget("text")
    e1.config(state='normal')
    e1.insert(tk.END, a1)
    e1.config(state='readonly')

def delete():
    """Backspace logic: deletes the last character or resets to '0'."""
    global c1, c2
    c1 = e1.get()
    c2 = len(c1)
    if c2 <= 1: # If only one character left, reset to '0'
        e1.config(state='normal')
        e1.delete(0, tk.END)
        e1.insert(tk.END, '0')
        e1.config(state='readonly')
    else: # Delete the last character
        e1.config(state='normal')
        e1.delete(len(e1.get()) - 1, tk.END)
        e1.config(state='readonly')

# Main Application Window Setup
ml = tk.Tk()
ml.title("kalkulators")
ml.geometry("300x400")

# --- Button Definitions and Placement ---
# Number Buttons
btn0 = tk.Button(ml, text="0", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt0)
btn0.place(x=95, y=320, width=50, height=50)

btn1 = tk.Button(ml, text="1", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt1)
btn1.place(x=45, y=270, width=50, height=50)

btn2 = tk.Button(ml, text="2", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt2)
btn2.place(x=95, y=270, width=50, height=50)

btn3 = tk.Button(ml, text="3", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt3)
btn3.place(x=145, y=270, width=50, height=50)

btn4 = tk.Button(ml, text="4", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt4)
btn4.place(x=45, y=220, width=50, height=50)

btn5 = tk.Button(ml, text="5", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt5)
btn5.place(x=95, y=220, width=50, height=50)

btn6 = tk.Button(ml, text="6", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt6)
btn6.place(x=145, y=220, width=50, height=50)

btn7 = tk.Button(ml, text="7", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt7)
btn7.place(x=45, y=170, width=50, height=50)

btn8 = tk.Button(ml, text="8", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt8)
btn8.place(x=95, y=170, width=50, height=50)

btn9 = tk.Button(ml, text="9", bg='grey', fg='white', font=('arial', 14, 'bold'), command=ins_txt9)
btn9.place(x=145, y=170, width=50, height=50)

# Operator Buttons
btn10 = tk.Button(ml, text="+", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en0)
btn10.place(x=195, y=170, width=50, height=50)

btn11 = tk.Button(ml, text="-", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en1)
btn11.place(x=195, y=220, width=50, height=50)

btn12 = tk.Button(ml, text="/", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en3)
btn12.place(x=195, y=270, width=50, height=50)

btn13 = tk.Button(ml, text="*", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en2)
btn13.place(x=195, y=320, width=50, height=50)

btn14 = tk.Button(ml, text="=", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en4)
btn14.place(x=145, y=320, width=50, height=50)

btn17 = tk.Button(ml, text="x^n", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en5)
btn17.place(x=95, y=120, width=50, height=50)

btn18 = tk.Button(ml, text="√", bg='grey', fg='white', font=('arial', 14, 'bold'), command=g_en6)
btn18.place(x=145, y=120, width=50, height=50)

# Functional Buttons (Clear, Dot, Backspace)
btn15 = tk.Button(ml, text="C", bg='grey', fg='white', font=('arial', 14, 'bold'), command=cl_e1)
btn15.place(x=45, y=120, width=50, height=50)

btn16 = tk.Button(ml, text=".", bg='grey', fg='white', font=('arial', 14, 'bold'), command=dot)
btn16.place(x=45, y=320, width=50, height=50)

btn19 = tk.Button(ml, text="⌫", bg='grey', fg='white', font=('arial', 14, 'bold'), command=delete)
btn19.place(x=195, y=120, width=50, height=50)

# Output Display (Entry)
e1 = ttk.Entry(ml, font=('arial', 12))
e1.place(x=46, y=60, width=200, height=30)
e1.config(state='readonly') # Start as read-only to prevent keyboard typing

ml.mainloop()