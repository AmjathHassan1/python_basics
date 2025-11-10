# Oops questions
#
# 1.Write a program to create a class Employee with attributes name and salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Add a method to display the employee details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def employee_details(self):
        return f'Name: {self.name}\nSalary: {self.salary}'


# 2.Create a class named Student with attributes name and age. Create two objects and print their details.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_details(self):
        return f'Name: {self.name}\nAge: {self.age}'
student1=Student('Amjath', 20)
student2=Student('Hassan', 23)
print(student1.student_details())
print(student2.student_details())

# 3.Create a class Circle that has a method to calculate the area and circumference using the radius.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circle_area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 3.14 * 2 * self.radius

circle=Circle(5)
print(circle.circle_area())
print(circle.circumference())


# 4.Create a class Person with a constructor (__init__) that initializes name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create two objects with different details and print them

p = Person('Amjath', 20)
print(p.name)
print(p.age)
p1=Person('Amjath Hassan', 20)
print(p1.name)
print(p1.age)

# 5.Create a class Parent with an attribute name and a method display().

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name
p1=Parent('Amjath Hassan')
print(p1.display())

# Create a class Child that inherits from Parent and displays both parent and child names.

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
    pass
c1=Child("Amjath")
print(c1.display())

# 6.Create two classes Cat and Dog, each having a method make_sound().

class Cat:
    def make_sound(self):
        print('Mewow')

class Dog:
    def make_sound(self):
        print('BOW')

# Write a common function that calls make_sound() for any object.

cat=Cat()
dog=Dog()

def make_sound(animal):
    animal.make_sound()

make_sound(cat)
make_sound(dog)