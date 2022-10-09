import tkinter as tk
import random

win = tk.Tk()
canvas=tk.Canvas(win,width=400,height=450, bg="grey")
canvas.pack()
voda=[]
zem =[]
piczem = tk.PhotoImage(file="ostrov0.png")
picvoda = tk.PhotoImage(file="images/ostrov3.png")
obrazky = [tk.PhotoImage(file="images/ostrov_kruh0.png"),tk.PhotoImage(file="images/ostrov_kruh1.png")]
mosty = [tk.PhotoImage(file="images/ostrov1.png"),tk.PhotoImage(file="images/ostrov2.png")]
sirobr=50
vysobr=50
prepinatko=0
peniaz=0


def create_screen():
    m=random.randrange(4,7)
    n=random.randrange(3,10)
    for stlpec in range(n+1):
        for riadok in range(m+1):
            temp=random.randint(1,5)
            if temp==1:
                temp=piczem
            else:
                temp=picvoda
            temp=canvas.create_image(riadok*sirobr, stlpec*vysobr ,image=temp, anchor="nw")
            zem.append(temp)

def preinac(e):
    global prepinatko
    if canvas.itemcget("switcher","image")=="pyimage3":
        canvas.itemconfig("switcher",image=obrazky[1])
        prepinatko = 1
    elif canvas.itemcget("switcher","image")=="pyimage4":
        canvas.itemconfig("switcher",image=obrazky[0])
        prepinatko = 0
    print(prepinatko)

def presneto(e):
    global prepinatko,peniaz,text
    if prepinatko == 0:
        x = (e.x//50)*50
        y = (e.y//50)*50
        id=canvas.find_withtag("current")[0]
        canvas.delete(id)
        canvas.create_image(x, y, image = mosty[0], anchor = "nw", tags="bridge")
        peniaz += 10
    elif prepinatko==1:
        x=(e.x//50)*50
        y=(e.y//50)*50
        id=canvas.find_withtag("current")[0]
        canvas.delete(id)
        canvas.create_image(x,y,image=piczem,anchor="nw")
        peniaz += 50
    text.config(text=peniaz)

def tocimsa(e):
    global prepinatko
    if prepinatko==0:
        if canvas.itemcget("current","image")=="pyimage5":
            canvas.itemconfig("current",image=mosty[1])
        elif canvas.itemcget("current","image") == "pyimage6":
            canvas.itemconfig("current",image=mosty[0])

def pocitadlo(e):
    global peniaz
    text.config(text=peniaz)



create_screen()
canvas.tag_bind("switcher","<Button-1>", preinac)
canvas.tag_bind("water","<Button-1>",presneto)
canvas.tag_bind("bridge","<Button-1>",tocimsa)
canvas.bind("<Button-1>",pocitadlo)
win.mainloop()