# modules

# modules <packages><libraries>


# built-in modules, user, defined modules

# math, random, sys, os , time


import math

help(math)

a=math.factorial(5)

print(a)


import calendar

a=calendar.calendar(2025)
print(a)

b=calendar.month(2025, 10)
print(b)


import os

print(os.getcwd)

# os.mkdir(r"path/dir_name")

print(os.listdir('Assignments'))


import test_module  

sum= test_module.sum(1,3)
print(sum)


test_module.print_hello()



# file handling


'''
f1=open("test_file.txt", "r")

print(f1.read()) # read the whole file
print(f1.read(5)) # read the whole file
print(f1.readlines())
print(f1.readline())

#f1.close()
'''


'''
f2=open("test_file.txt", "w")


f2.write("PYTHON IS SIMPLE")

f2.close()



f1=open("test_file.txt", "r")

print(f1.read())

'''



































