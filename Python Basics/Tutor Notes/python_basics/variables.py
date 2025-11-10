#variables

#variables are used to store and manage data values.
#it is basically a storage space

#print(5)


x=5
print(x)

y=4.5

print(y)

name="sona"
print(name)

print("my name is",name)

a=10000
b=100

print("the sum of two numbers is",a+b)


#variable rules

#it should start with a letter or underscore(both uppercase and lowercase are allowed)

#*name="sona"

#print(*name)

#it cant start with a number

#9name="sona"

#print(9name)

#it can only contain alpha-numeric characters
#(space,symbols ?,*,&.....)
'''
number1=10
print(number1)
my name="sona"
print(my name)
'''

#python is case sensitive

age=10
AGE=20
Age=30

print(age)

#KEYWORDS can not be used as variable names

#if,else,for,while,and,or,not....

#for="sona"
#print(for)
'''
my var=5
my-var=6
my_var=7
name1="sona"
1name="sona"
or="sona"
'''

#many values to multiple variables

x,y,z,="a","b","c"

print(x)
print(y)
print(z)

#one value to multiple variables
'''
x=y=z=a="python"

print(x)
print(y)

a=10
a="entri"
print(a)
'''
#casting

#casting means changing /converting the datatype of a variable from one
#type to another

'''
x="10" #string
print(type(x))

y=int(x)
print(y)
print(type(y))
'''
a=3.5

print(int(a))


a=5
print(float(a))


a=0
print(bool(a))


a=12
print(bool(a))

a=[]
print(bool(a))


a=3
print(str(a)) #"3"


a=3
print(type(a))

b=float(a)#3.0
print(type(b))


print(bool(5))
print(bool(""))
print(bool("hiiiii"))
print(bool({})


#
'''
a="1000"
print(int(a))
print(float(a))

a="sona"
print(int(a))

'''
#input()

#it is used to take inputs from end users

name=int(input(''))
print(name)
print(type(name))

'''
a="5"
b="6"
y=a+b
print(y)
x=int(a)+int(b)
print(x)
'''
print(3+5)

print(10<100)





































