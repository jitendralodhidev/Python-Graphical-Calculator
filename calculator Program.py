
from tkinter import *
import tkinter.messagebox as tsmg
root=Tk()
root.geometry("400x600")
root.title("Calculator ")
root.config(background="grey")
root.wm_iconbitmap("calculator.ico")

# function for button click

def click(event):
    global value
    
    #here .cget help us to get the value from the event widget
    
    text = event.widget.cget("text")
    print(text)
    if text == "=":
       if value.get().isdigit():
            result=int(value.get())
       else:
           try:
            result=eval(screen.get())
            value.set(result)
           except Exception as e:
               print(e)
               value.set("error")
               screen.update()
    elif text =="C":
        value.set("")
        screen.update()
    else:
        value.set(value.get() + text)
        screen.update()
        
 #function for exit option 

def confirm():
    choice=tsmg.askyesno("exit","Exit Calculator ")
    print(choice)
    if choice == True:
        quit()
    else:
        pass
menu=Menu(root)
menu.add_command(label="exit",command = confirm)
root.config(menu=menu)

# label for heading
Label(text="CALCULATOR",font="lucida 18 bold", bg="grey").pack(padx=6,pady=6)
value = StringVar()
value.set("")

# displaying screen 

screen = Entry(root, textvar=value, font=" lucida 18 bold")
screen.pack(fill=X,padx=25,pady=25)
f = Frame(root, bg="grey")

# for loop for creating button upto 1-3

for i in range (3):
    b = Button(f,text=f"{i}", font=" lucida 30 bold")
    b.bind("<Button-1>", click)
    b.pack(side=LEFT,padx=2,pady=2)
    i=i+1
b = Button(f,text="+",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(padx=2,pady=2)
f.pack()
f = Frame(root,bg  ="grey")

# for loop for creating button upto 3-6

for i in range (3,6):
    b=Button(f,text=f"{i}",font="lucida 30 bold")
    b.bind("<Button-1>", click)
    b.pack(side=LEFT,padx=2,pady=2)
    i=i+1
b=Button(f,text="-",font="lucida 32 bold")
b.bind("<Button-1>", click)
b.pack(padx=5,pady=6)
f.pack()
f = Frame(root,bg  ="grey")

# for loop for creating button upto 6-9

for i in range (6,9):
    b=Button(f,text=f"{i}",font="lucida 30 bold")
    b.bind("<Button-1>",click)
    b.pack(side=LEFT,padx=2,pady=2)
    i=i+1
b=Button(f,text="*",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(padx=2,pady=2)
f.pack()
f = Frame(root,bg  ="grey")

#creating additional buttons and packing them 

b=Button(f,text="9",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="C",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="=",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="/",font="lucida 30 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=5,pady=8)
f.pack()
root.mainloop()
