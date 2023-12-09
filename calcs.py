from tkinter import *
import ast

i=0
j=0

def allClear():
    disp.delete(0,END)

def di(st):
    global i
    disp.insert(i,st)
    i+=1

def dlt():
    global j
    h=disp.delete(i-j,i)
    j+=1    

def calculate(fun_str):
    node=ast.parse(fun_str,mode="eval")
    try:
        ret=eval(compile(node,'<string>','eval'))
        allClear()
        disp.insert(0,ret)
    except Exception as e:
        allClear()
        disp.insert(0,e)

# Main calculater
    
root=Tk()
disp=Entry(root,width=35,borderwidth=5,bd=5)
disp.grid(row=0,column=0,columnspan=3,padx=40,pady=40)

n1=Button(root,text='1',padx=40,pady=20,command=lambda:di('1')).grid(row=1,column=0)
n2=Button(root,text='2',padx=40,pady=20,command=lambda:di('2') ).grid(row=1,column=1)
n3=Button(root,text='3',padx=40,pady=20,command=lambda:di('3') ).grid(row=1,column=2)
n4=Button(root,text='4',padx=40,pady=20,command=lambda:di('4') ).grid(row=2,column=0)
n5=Button(root,text='5',padx=40,pady=20,command=lambda:di('5') ).grid(row=2,column=1)
n6=Button(root,text='6',padx=40,pady=20,command=lambda:di('6') ).grid(row=2,column=2)
n7=Button(root,text='7',padx=40,pady=20,command=lambda:di('7') ).grid(row=3,column=0)
n8=Button(root,text='8',padx=40,pady=20,command=lambda:di('8') ).grid(row=3,column=1)
n9=Button(root,text='9',padx=40,pady=20,command=lambda:di('9') ).grid(row=3,column=2)
n0=Button(root,text='0',padx=40,pady=20,command=lambda:di('0') ).grid(row=4,column=1)
# Calcualte Functioning Buttons
add=Button(root,text='+',padx=40,pady=20,command=lambda:di('+') ).grid(row=4,column=0)
sub=Button(root,text='*',padx=40,pady=20,command=lambda:di('*') ).grid(row=4,column=2)
mul=Button(root,text='-',padx=40,pady=20,command=lambda:di('-') ).grid(row=5,column=0)
div=Button(root,text='/',padx=40,pady=20,command=lambda:di('/') ).grid(row=5,column=2)
eql=Button(root,text='=',padx=40,pady=20,command=lambda:calculate(disp.get())).grid(row=6,column=1)
dlet=Button(root,text='Dlt',padx=40,pady=20,command=dlt).grid(row=6,column=0)
ac=Button(root,text='AC',padx=40,pady=20,command=allClear,fg="red").grid(row=5,column=1)

root.mainloop()