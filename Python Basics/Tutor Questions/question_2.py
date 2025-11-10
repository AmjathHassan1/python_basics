# Conditional statements questions
#
# 1.write a program to find the smallest of two numbers input by the user


# num_1=float(input("Enter the first number: "))
# num_2=float(input("Enter the second number: "))
#
# if num_1>num_2:
#     print("The first number is greater than the second number")
# elif num_1<num_2:
#     print("The first number is less than the second number")
# else:
#     print("Both numbers are equal")

# =======================================================================

# 2.write a program to find the largest of 3 numbers input by the user

# num_1=float(input("Enter the first number: "))
# num_2=float(input("Enter the second number: "))
# num_3=float(input("Enter the third number: "))
#
# if num_1>num_2:
#     if num_1>num_3:
#         print("The first number is larget", num_1)
#     elif num_3>num_1:
#         print("The third number is largest", num_3)
# else:
#     if num_2>num_3:
#         print("The second number is largest", num_2)
#     else:
#         print("The third number is largest", num_3)


# ================================================

# 3.write a program to check a number is positive ,negative or zero
# Eg:input : -10
# Output :negative

# num=int(input("Enter a number: "))
# if num<0:
#     print("negative")
# elif num>0:
#     print("positive")
# else:
#     print("zero")

# ====================================================

# 4.write a program to find whether a number is even or odd input by the user
# Eg :input :26
# Output :even (hint :use modulus operator)

# num=int(input("Enter a number: "))
#
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# ========================================================

# 5.write a program to check a person is eligible for voting based on the age input by the user
# Eg :input :25
# Output:eligible


# age=int(input("Enter your age: "))
# if age>=18:
#     print("eligible")
# else:
#     print("not eligible")

#  ==============================================================


# 6.write a program to print "hello world " if user inputs "Hai ",else print "bye..."

# word=input("Enter a word: ")
# if word=="Hai ":
#     print("hello world ")
# else:
#     print("bye...")

# =================================================================

# 7.write a program to calculate the discount of an amount input by the user

# If amount >10000,discount =10 %
# If amount is bw 10000 and 5000 ,discount=5%
# Else,no discount

# Eg:
# Input :8000
# Output:discounted amount=7600

amount=float(input("Enter the amount: "))
if amount > 10000:
    discount=10
    discounted_amount=amount-amount*discount/100
    print("discounted amount=",discounted_amount)
elif 5000 < amount < 10000:
    discount = 5
    discounted_amount = amount - amount * discount / 100
    print("discounted amount=", discounted_amount)
else:
    print("No discount")