# Module questions
#
# 1.calculate 5³ using math module

import math
n=5
print(n)
print(math.pow(n,3))

# 2.Round 5.67 down using math.floor() and up using math.ceil().

n=5.67
print(math.floor(n))
print(math.ceil(n))

# 3.find both natural logarithm and base 10 logarithm values of 100.

n=100
print(math.log(n,2))
print(math.log10(n))


# 4.Find the greatest common divisor (GCD) of two numbers.



# 5.Write a program to find the area of a circle using math.pi.radius input by the user.

rad=float(input("Enter the radius: "))
print("Area of circle:",math.pi*rad**2)

# 6.Calculate the value of sin(30°), cos(60°), and tan(45°) using the math module.

print(math.sin(30))
print(math.cos(60))
print(math.tan(45))

# 7.Import the calendar module and print the calendar for the year 1998

import calendar
print(calendar.calendar(1998))

# 8.print the calendar of August 2025

print(calendar.month(2025,themonth=8))

# 9.Print the weekday of a specific date (e.g., 15th August 2024) using calendar.weekday().

print(calendar.weekday(2024,8,15))

# 10.Display the number of leap years from year 2000 to the current year.

print(calendar.leapdays(2000,2025))

# 11.Import the random module and generate a random integer between 1 and 10.

import random
print(random.randint(1, 10))

# 12.Select a random element from a list of colors using random.choice().

colors=['red','green','blue','yellow','magenta','cyan']
print(random.choice(colors))

# 13.Shuffle a list of numbers using random.shuffle() and print it.

random.shuffle(colors)
print(colors)