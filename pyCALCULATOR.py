from tkinter import *

def write(x): #function to write the pressed numberson the screen
    s = len(entry.get())
    entry.insert(s,str(x))
    print(x)

oper = 5
s1 = 0
def operations(x):
    global oper
    oper = x
    global s1
    s1 = float(entry.get())
    entry.delete(0,'end')

s2 = 0
def calculate():
    global s2
    s2 = float(entry.get())
    global oper
    result = 0
    if(oper==0): 
        result = s1 + s2
    elif(oper==1):
        result = s1 - s2
    elif(oper==2):
        result = s1 * s2
    elif(oper==3):
        result = s1 / s2
    entry.delete(0,'end')
    entry.insert(0,str(result))

frame = Tk()
frame.geometry("240x300")

entry = Entry(font="Verdana 14 bold", width=15,justify=RIGHT)
entry.place(x=20,y=20)

b = []
for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:write(x)))
counter =0
for i in range(0,3):
    for j in range(0,3):
        b[counter].place(x=20+i*50,y=50+j*50)
        counter +=1

op = []
for i in range(0,4):
    op.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:operations(x)))

op[0]['text'] = "+"
op[1]['text'] = "-"
op[2]['text'] = "*"
op[3]['text'] = "/"

for i in range(0,4):
    op[i].place(x=170,y=50+50*i)

sb = Button(text="0", font = "Verdana 14 bold",command=lambda x=0:write(x)) #button placement
sb.place(x=70,y=200)

db = Button(text=". ", font = "Verdana 14 bold",width=2,command=lambda x=".":write(x))
db.place(x=120,y=200)

eb = Button(text="=", font = "Verdana 14 bold",command=calculate) #no paranthesis in calculate
eb.place(x=170,y=250)

frame.mainloop()
