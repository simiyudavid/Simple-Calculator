from operator import imod
from re import A
from turtle import color


'''a = 2000
if a > 20:
    print("a is above 20")
    if a>300:
        print("and also above 300")

    else:
        print("but not above 300")

else:
    print("Lets go")

i = 10
while i<6:
    print(i)
    i=i+1

else:
    print("i is no longer less than 6")

adj = ["red","big","tasty"]
fruits = ["apple", "banana", "cherry"]
deivy = ["simiyu", "balin", "mato"]

for x in adj:
    for y in fruits:
        for z in deivy:
            print(x,y,z)

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Deivy", 23)

p1.myfunc()


class Person:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student (Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.fname)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(myit)
print(next(myit))
print(next(myit))


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Len")
x.printname()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x

        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

def myfunc():
    global x
    x = 300
    print(x)
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

def deivy():
    print(x)

import deivy

deivy.greetings("Simiyu")

import platform

x = dir(platform)
print(x)

from math import sqrt

x = sqrt(16)

print(x)

import tkinter as tk

from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)

w = Spinbox(master, from_ = 0, to = 10)
w.grid(row=4, column=1)

w.insert(END, 'Select Your Level')
w = Text(height=2, width=30)
mainloop()

from tkinter import *

root = Tk()
mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text="My name is Simiyu David")
mylabel3 = Label(root, text=" ")
mylabel4 = Label(root, text=" ")
 
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=4, column=7)
mylabel3.grid(row=2, column=5)
mylabel4.grid(row=3, column=6)

mainloop()'''

from tkinter import *

root = Tk()
root.title("Simple calculator")

e = Entry(root, width=50, borderwidth=10, bg="RED", bd=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(1, "Enter your name")

'''def myClick():
    mylabel = Label(root, text=e.get())
    mylabel.pack()
mybutton = Button(root, text="Enter your name", bg="red", fg="blue", padx=50, pady=10, command=myClick)
'''

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) 

def button_clear():
    e.delete(0, END)


def button_add():
    global first_number
    global f_num
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

button1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1), bg="RED", bd=10)
button2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2), bg="PINK", bd=10)
button3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3), bg="GREY", bd=10)
button4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4), bg="BROWN", bd=10)
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5), bg="YELLOW", bd=10)
button6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6),bg="GREEN", bd=10)
button7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7), bg="BLUE", bd=10)
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8), bg="ORANGE", bd=10)
button9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9), bg="#00ff00", bd=10)
button0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0), bg="#800000", bd=10)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="#800080", bd=10)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal, bg="#000080", bd=10)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear, bd=10)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


mainloop()


