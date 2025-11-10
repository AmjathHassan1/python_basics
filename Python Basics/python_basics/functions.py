# functions

#print(10+12)

#built-in functions -> print(), input(), type(), id()

#user defined functions

# def function_name():   #function declaration
    #function_body
    # return statement
# function_name() # function call

'''

def f_name():
    print("Hello world")
f_name()
'''

def product(num1, num2):  # arguments
    print(num1 * num2)

product(1,3) # parameters


#positional arguments : arguments are passed based on the position


'''
def square(a):
    print(a**2)

square(5)
'''

# default arguments

'''
def name(firstname, lastname="abu"):
    print("my first name is", firstname, " my last name is ", lastname)
name("Amjath","Hassan")
name("Amjath")

'''

# keyword arguments

'''
def name(firstname, lastname="abu"):
    print("my first name is", firstname, " my last name is ", lastname)
name(lastname="Amjath",firstname="Hassan")
name(lastname="Hassan",firstname="Amjath")

'''

# arbitrary argument

'''
def add(*a):  #  a=(1, 2,3, 4, 5)
    sum=0
    for i in a:
        print(i)
        sum+=i
    print(a)
    print(sum)
add(1, 2, 3, 4, 5)
'''

# function with return type


'''
def add(a, b):
    return a+b
sum=add(2, 4)
print(sum)

'''

# lambda functions : sngle anonymous function
# variable_name=lambda arguments:expression

'''
sum=lambda x, y: x+y
print(sum(10, 29))
'''

check = lambda a: a**2 if a>0 else None
print(check(5))
























