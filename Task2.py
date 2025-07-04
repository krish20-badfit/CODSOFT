import tkinter 
from fractions import Fraction

r = tkinter.Tk()

r.title("CALCULATOR")

r.geometry("260x350")
r.config(bg="#3b3b3b")

exp=""
f= True
calculator=False
calculated=0




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
        exp+="+"
        return
    if t=="x":
        exp+="*"
        return
    exp+=t



def click(event):
    global exp
    global f 

    t = event.widget.cget("text")
    if screenvar.get()!="ERROR PRESS C":

        if t=="C":
            clear()

        elif t=="%":
            screenvar.set(screenvar.get()+t)
            exp+="/100"

        elif t=="S<>D":
            frac()
        elif t=="=":
            calculate()
        else:
            numerator(t)
    else:
        if t=="C":
            clear()


f1 = tkinter.Frame(r,bg="black")


screenvar=tkinter.StringVar()
screenentry=tkinter.Entry(f1,width=30,text=screenvar,fg="black",bg="#e5f2e5",font=("Eurostile",15,"bold"),justify="right")
screenentry.pack(fill="x")


l=tkinter.Label(f1,bg="black")
l.pack()
f1.pack(fill="x")

f2=tkinter.Frame(r,bg="#3b3b3b")
button=tkinter.Button(f2,text="OFF",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"),command=quit)
button.grid(row=0,column=0,padx=8,pady=8)
button=tkinter.Button(f2,text="S<>D",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=0,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="%",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=0,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="/",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=0,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="7",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=1,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="8",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=1,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="9",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=1,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="x",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=1,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="4",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=2,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="5",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=2,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="6",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=2,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="-",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=2,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="1",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=3,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="2",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=3,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="3",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=3,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="+",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=3,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="C",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=4,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="0",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=4,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text=".",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=4,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="=",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))
button.grid(row=4,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)
f2.pack(pady=15)



r.mainloop()