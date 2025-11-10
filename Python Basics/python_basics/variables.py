# variables

# variables are used to store and manage data values
# It is basically a stogae space

print(5)

x=5
print(x)

y=4.5
print(y)

name = 'amjath'
print(name)

print(f"my name is", name)
print(f"my name is {name}")

a = 10
b= 20
print("the sum of two number is", a+b)


#variable rule

#It should start with a letter or underscore(both uppercase and lowercase are allowed)
#It cant start with a number
#it can only contain alpha-numeric characters
#(space, symbols ?,*,& .....)
#python is case sensitive
#KEYWORDS can not be used as variables name


#many values to multiple variables

x, y, z="a", "b", "c"
print(x)
print(y)
print(z)

#one value to multiple variable

x=y=z="python"
print(x)
print(y)
print(z)

a=20
b="twenty"
print(b)
print(id(z))


#casting means changing or converting the data type of a variable from one to another

'''
x="10" # sting
y=int(x)
print(type(x))
print(y)
print(type(y))
'''


a=3.5
print(int(a))


a=5
print(float(a))

b=10
print(bool(b))

c=""
print(bool(c))

d=0
print(bool(d))

a=3
print(str(a), type(str(a)))

print(list("amjath"))



'''
int() - constructs an integer number from an integer literal, 
a float literal (by removing all decimals), or a string literal 
(providing the string represents a whole number)



float() - constructs a float number from an integer literal, 
a float literal or a string literal 
(providing the string represents a float or an integer)



str() - constructs a string from a wide variety of data types, 
including strings, integer literals and float literals
'''


#input()
#it is used to take imputs from the user : default str
name=input("")
print(name)
print(type(name))

'''
a='5'
b='6'
x=int(a)+int(b)
print(x)

name=int(input(""))
print(name)
print(type(name))
'''


