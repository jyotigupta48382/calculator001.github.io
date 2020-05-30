import tkinter
root=tkinter.Tk()
root.geometry("295x660")
screen_value=tkinter.StringVar()
screen_value.set("")
screen=tkinter.Entry(root,textvar=screen_value,font="bold",bg="cyan",fg="black")
screen.grid(ipadx=56,columnspan=5,ipady=8)


exp =""
def enter(num):
    global exp
    exp += str(num)
    return screen_value.set(exp)

def result(eqn):
    global exp
    result=eval(eqn)
    return screen_value.set(result)
    

    
        

def clearscr():
    global exp
    exp=""
    return screen_value.set(exp)

b0=tkinter.Button(root,command=lambda:enter(0),text="0",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b1=tkinter.Button(root,command=lambda:enter(1),text="1",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b2=tkinter.Button(root,command=lambda:enter(2),text="2",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b3=tkinter.Button(root,command=lambda:enter(3),text="3",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b4=tkinter.Button(root,command=lambda:enter(4),text="4",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b5=tkinter.Button(root,command=lambda:enter(5),text="5",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b6=tkinter.Button(root,command=lambda:enter(6),text="6",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b7=tkinter.Button(root,command=lambda:enter(7),text="7",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b8=tkinter.Button(root,command=lambda:enter(8),text="8",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b9=tkinter.Button(root,command=lambda:enter(9),text="9",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b02=tkinter.Button(root,command=lambda:enter("-"),text="-",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b03=tkinter.Button(root,command=lambda:enter("+"),text="+",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b04=tkinter.Button(root,command=lambda:enter("/"),text="/",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b05=tkinter.Button(root,command=lambda:result(screen_value.get()),text="=",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b06=tkinter.Button(root,command=lambda:enter("*"),text="*",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b07=tkinter.Button(root,command=lambda:enter("**"),text="**",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b08=tkinter.Button(root,command=lambda:enter("."),text=".",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b09=tkinter.Button(root,command=lambda:enter("("),text="(",font="blod",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b00=tkinter.Button(root,command=lambda:enter(")"),text=")",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
b21=tkinter.Button(root,command=lambda:clearscr(),text="clear",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=7)
e=tkinter.Button(root,command=root.destroy,text="exit",font="bold",activeforeground="light blue",activebackground="#00FFFF",bg="light blue",height=5,width=28)


                   
b21.grid(row=3,column=1)                 
b09.grid(row=3,column=2)                   
b00.grid(row=3,column=3)
b08.grid(row=3,column=4)
b07.grid(row=4,column=1)                   
b06.grid(row=4,column=2)                   
b05.grid(row=4,column=3)
b04.grid(row=4,column=4)
b03.grid(row=5,column=1)                   
b02.grid(row=5,column=2)                   
b9.grid(row=5,column=3)
b8.grid(row=5,column=4)
b7.grid(row=6,column=1)                   
b6.grid(row=6,column=2)
b5.grid(row=6,column=3)
b4.grid(row=6,column=4)
b3.grid(row=7,column=1)                   
b2.grid(row=7,column=2)                   
b1.grid(row=7,column=3)
b8.grid(row=7,column=4)
b0.grid(row=5,column=4)
e.grid(row=8,columnspan=5)


root.mainloop() 
