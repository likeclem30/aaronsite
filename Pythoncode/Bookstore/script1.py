"""
The program that store this book information
Title, Authur
Year , ISBN

User can
view all Record
Search an entry
Add entry
Update entry
Delete
Close

"""

from tkinter import *

window = Tk()
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Authur")
l2.grid(row=0,column=2)

l1 = Label(window,text="Year")
l1.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

authur_text = StringVar()
e2 = Entry(window,textvariable=authur_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all" ,width=12)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry" ,width=12)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry" ,width=12)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected" ,width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected" ,width=12)
b5.grid(row=6,column=3)

b6=Button(window,text="Closed" ,width=12)
b6.grid(row=7,column=3)


window.mainloop()