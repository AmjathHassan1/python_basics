# Conditional statement

print("hello world")
#if, elif, else

'''
#syntax
#if (condiation):
    # body of the condition
'''

'''
num=int(input("enter a number : "))
if num==10:
    print(num,"is 10")
    print("hello world")
else:
    print(num,"is not 10")
'''

'''num=int(input("enter a number : "))
if num==10:
    print(num,"is 10")
    print("hello world")
elif num==20:
    print(num,"is 20")
    print("hello world")

else:
    print(num,"is not 10")'''

# Qn: Find the largest number

num1=int(input("enter a number 1: "))
num2=int(input("enter a number 2: "))
if num1==num2:
    print("equal")
elif num1>num2:
    print("num1 is greater")

else:
    print("num1 is lesser")