#oop

#object oriented programming

#class,object,abstraction,encapsulation,polymorphism,inheritance

#modularity

#class

#collection of objects
#blueprint of an object
#collection of properties and behaviours of an object

#object
#instance of a class


#eg
#class-car    objects-alto,toyota
#class-class objects-students
#class-laptop   objects-hp,lenovo

'''
class A:
    def fun1(self):
        print("function1")
    def fun2(self):
        print("function2")
obj=A()#object creation of class A

obj.fun1()
obj.fun2()

'''
#create a class "math" .create two functions inside that class
#1.sum of two nums
#2.product of two numbers
'''
class math:
    def sum(self,a,b):
        print(a+b)
    def pro(self,a,b):
        print(a*b)
obj=math()
obj.sum(10,46)
obj.pro(6,10)
'''

#__init__  (constructor)
#the method lets the class to initialize the object values directly into a class
#while calling

class math:
    def __init__(self,a,b):
        print(a+b)
        
obj=math(20,30)
#obj.__init__(30,40)

obj2=math(50,40)

#create a class using constructor and generate 2 objects

#class:bike price,model


class student:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
        
obj=student("sona",27)

print(obj.age)

#self.name,self.age =object variables/instance variable 

#self :self refers to the current object (instance) being created from the class.


#class variables

#it is a variable that is shared by all objects of a class
'''
class student:
    company_name="entriapp"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
obj=student("sona",27)
obj2=student("megha",20)

print(obj.company_name)
print(obj2.company_name)

  

class student:
    def __init__(self,name,age):
        self.__name=name#private
        print(self.__name)
obj=student("sona",27)

print(obj.name)

'''
#inheritance

#inheritance means one class (the child class /derived class) can use the
#properties and methods of another class(parent class/base class)

#single inheritance
#multiple inheritance
#multileval inheritance
#heirarchical inheritance
#hybrid


#single inheritance
class A:#parent class
    def a(self):
        print("hello")
class B(A):#child class
    def b(self):
        print("good noon")
obj=B()
obj.a()
obj.b()

#create a parent class "school" having the function "details" which displays
#schoolname and location
#create a child class "student" that inherits the parent class having the
#function "studentdetails" which displays rollnum and batch 

#method overriding

#it happens when a child class defined a method with the same name as a method
#in its parent class
'''
class Animal:
    def sound(self):
        print("animals make sound")

class dog(Animal):
    def sound(self):
        print("dog barks")
obj=dog()
obj.sound()
'''
#here the child's version replaces (overrides) the parent's version.

#super method:it is used to 


class Animal:
    def sound(self):
        print("animals make sound")

class dog(Animal):
    def sound(self):
        super().sound()#calls the parent class
        print("dog barks")
d=dog()
d.sound()

#polymorphism
#the ability to exist in more than one form

#sound()

#function polymorphisms
print(5+10)#15,510#addition

print("sona"+"Rajan")#concatenation

print(len("sona"))

print(len([1,2,3,4,5,6]))


#multi leval inheritance

class Animal:
    def eat(self):
        print("all animals eat")
class mammals(Animal):
    def walk(self):
        print("mammals walk")
class dog(mammals):
    def bark(self):
        print("dogs bark")
obj=dog()
obj.eat()
obj.walk()
obj.bark()

#public,__

#encapsulation














