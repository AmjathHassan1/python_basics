# oop

# object oriented programming

# class, object, abstraction, encapsulation, polymorphism, inheritence

# modularity : single program can be resolved via partition

# class : collection of objects/blueprint of an object
# collection of properties and behaviour of an object

# object : instance of a class
# eg
# class-car     objects-alto, toyota


'''
class A:
    def func1(self):      # methods
        print("In func1")
    def func2(self):
        print("In func2")

obj_A = A()  # object creation of class A
obj_A.func1()
obj_A.func2()
'''


# Create a class Math create two functions inside that class
# 1. sum of two number
# 2. product of two number


'''
class Math():
    def sum(self, a, b):
        return a + b
    def product(self, a, b):
        return a * b

math_obj=Math()
print(math_obj.sum(1,2))
print(math_obj.product(2,3))
'''


# __init__ (constructor)
# the meothod lets to class to initialize the object values
# directly into a class while calling

'''
class Math():
    def __init__(self, a, b):
        print("Init called")
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def product(self):
        return self.a * self.b
print("before Init called")
math_obj=Math(2,3)
print("before Init called")
print(math_obj.sum())
print(math_obj.product())
'''

# create a class unsing constructor and generate 2 objects

# class:bike

'''
class Bike():
    def __init__(self, brand, model, price):
        print(brand, model, price)

yamaha=Bike("yamaha", "r15", "180000")
yamaha=Bike("kawazaki", "z900", "1800000")
'''


'''
class Student:
    def __init__(self, name, age):
        self.name=name         # public variables/ object variables
        self.age=age           # instance variable
obj=Student("amjath", 26)
print(obj.name)
print(obj.age)
'''

# self : self refers to the current object (instance)
#        being created from the class


# class variable
# it is a variable that is shared by all objects shared by a class

'''
class Student:
    company="Entri"    # class variable
    def __init__(self, name, age):
        
        self.name=name         # public variables/ object variables
        self.age=age           # instance variable
obj=Student("amjath", 26)
obj1=Student("hassan", 27)
print(obj.name)
print(obj.age)
print(obj.company)
print(obj1.name)
print(obj1.age)
print(obj1.company)

print(Student.company)
'''


'''
class Student:
    def __init__(self, name, age):
        self.__name=name # private variable
        print(self.__name)
        self.age=age
obj=Student("amjath", 26)
print(obj.age)
print(obj.__name)  # cannot be access becaude it private variable
'''

# inheritence

# inheritence means one class (the child class / derived class)
# can use propertirs and methods of another class(parent class/ base class)
        

# single inheritence
# multiple inheritence
# multi level inheritence
# heirarchial inheritance
# hybrid inheritence


'''
class A:   # parent class
    def a(self):
        print("Hello")

class B(A): # child class
    def b(self):
        print("World")

obj=B()
obj.a()
obj.b()

'''

# Create a parent clas School having the function details
# which displays schoo name and location
# create a child clsss student that inherits the parent class having
# the sunction student_details which display roll_number and batch


'''
class School():
    name = "Boys Attingal"
    location= "Attingal"


class Student(School):
    def __init__(self, roll_number, batch):
        self.roll_number =roll_number
        self.batch =batch
student1=Student(1, "A1")
print(student1.roll_number, student1.batch, student1.name, student1.location)
student2=Student(2, "A2")

'''


# Method Overriding
# It happens when a child class defined a method with the same name as
# as a methis in its parent class


'''
class Animal:
    def sound(self):
        print("animals make sound")

class Dog(Animal):
    def sound(self):
        print("dog barks")
        


obj=Dog()
obj.sound()
'''

# here the child's version replaces (overrides) the parents version

# super methods : it is used to calls the parent functionality

'''
class Animal:
    def sound(self):
        print("animals make sound")

class Dog(Animal):
    def sound(self):
        print("dog barks")
        super().sound()  # calls the parent class

obj=Dog()
obj.sound()
'''

# polymorphism
# the ability to exists in more that one form

#eg: sound()


# function polymorphisms

print(5+10)
print("amjath" + " Hassan")

# multi level inheritence

class Animal:
    def eat(self):
        print("all animals eat")

class Mammals(Animal):
    def walk (self):
        print("mammals walk")

class Dog(Mammals):
    def bark(self):
        print("dogs bark")

obj=Dog()
obj.eat()
obj.walk()
obj.bark()


# public, __

# encapsulation















































