#modules

#modules<packages<libraries


#built-in modules,user defined modules

#math,random,sys,os,time


import math

help(math)

a=math.factorial(5)
print(a)


print(math.sqrt(64))

print(math.pow(2,5))

print(math.ceil(2.3))
print(math.floor(2.3))

print(math.pi)

import calendar

help(calendar)

a=calendar.calendar(2025)
print(a)

b=calendar.month(2025,10)
print(b)

print(calendar.isleap(2025))

import os

print(os.getcwd())
#os.mkdir(r"C:\Users\we\Desktop\technical\newdir123")#raw string

#print("directory created successfully")


print(os.listdir(r"C:\Users\we\Desktop\technical"))


















