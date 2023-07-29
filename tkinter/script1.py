from tkinter import *   # * is import all

window=Tk()

def kmtomi():
    print(e1_val.get()) #get takes vslue from the variable(get is not used for input)
    miles=float(e1_val.get())*1.6
    t1.insert(END,miles) #END means concat


b1=Button(window,text="execute",command=kmtomi)
b1.grid(row=0,column=0) #can use pack or grid,grid divides window into grids therefore easy to place button

e1_val=StringVar() #this holds string value
e1=Entry(window,textvariable=e1_val)  #input
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20) #output
t1.grid(row=0,column=2)


window.mainloop()