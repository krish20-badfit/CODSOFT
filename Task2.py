import tkinter 
from fractions import Fractions

r = tkinter.Tk()
img = tkinter.PhotoImage(File='calculator.ico')
r.iconphoto(False,img)
r.title("CALCULATOR")

r.geometry("260x350")
r.config(bg="#3b3b3b")

exp=""
f= True
calculator=False




def calculate():
    global calculated
    global exp

    if screenvar.get()=="":
        return
    
    try:
        tmpexp=eval(exp)
        exp=str(Fraction(tmpexp).limit_denominator())
        screenvar.set(exp)
        calculated=True
    except:
        screenvar.set("Error press C")





def frac():
    global calculated
    global exp 
    global f 

    if calculated==1:
        tmpexp=Fraction(exp)
        if f==0:

            exp = str(tmpexp)
            screenvar.set(exp)
            f=1

        else:
            screenvar.set(str(tmpexp.numerator/tmpexp.denominator))
            f=0


def clear():
    global exp
    global f 
    global calculated

    screenvar.set("")
    exp=""
    calculated=0
    f=1

def numerator(t):
    global exp
    global f
    global calculated

    if calculated==1:
        screenvar.set("ANS")

        if t.isdigit():
            exp+=".."
        calculated=0
    
    screenvar.set(screenvar.get()+t)


    if t=="+":
        exp+="/"
        return
    if t=="x":
        exp+="*"
        return
    exp+=t



def click(event)