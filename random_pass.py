from tkinter import *
import random 
import string
def empty(r,c=0,w=1):
	label = Label(root,text="",width=w)
	label.grid(row=r,column=c)

def invalid():
		inval.config(text="(*invalid Level)",fg="red")
		
def copy_password():
	text=entry.get()
	if text !="":
		root.clipboard_clear()
		root.clipboard_append(text)
		root.update()
		label = Label(root,text="*password copied",fg="red").grid(row=4,column=2)
		
def GenratePass(length):
    if length.isdigit():
    	   length=int(length)
    	   if length > 15:
    	      inval.config(text="*please give length below 15", fg="red")
    	   else:
                chars = string.ascii_letters + string.digits + string.punctuation
                pas = "".join(random.choice(chars) for _ in range(length))
                entry.delete(0, END)
                entry.insert(0, pas)
    else:
    	invalid()

		
	


#main
root = Tk()

for i in range(10):
    empty(0,i,5)

title = Label(root,text="Random Password Gen..",fg="green",font=("Arial",15))
title.grid(row=1,column=3)

empty(2)
# Genrater
pwd = Label(root,text="Your Password : ").grid(row=3,column=1)
entry=Entry(root)
entry.grid(row=3,column=2)
copy=Button(root,text="Copy",padx=100,command=copy_password).grid(row=3,column=3)


empty(4)
#Password Length
length= Label(root,text="Length: ").grid(row=5,column=1)
entry1= Entry(root)
entry1.grid(row=5,column=2)

for i in range(5):
	empty(6,i,15)
	empty(7,i)
		
#Genrate Password
gen=Button(root,text="Generate ",padx=100,font=("Arial",10),command=lambda :GenratePass(entry1.get())).grid(row=8,column=2)

inval=Label(root,text="")
inval.grid(row=6,column=1)
root.mainloop()
