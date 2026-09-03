# 1)constructor and destructor:
# A constructor is a special method __init__() that is automatically called when an object is created.
# A destructor is a special method __del__() that is called when an object is destroyed.

# class Student:
#     def __init__(self):
#         print("Constructor called")

#     def __del__(self):
#         print("Destructor called")


# s = Student()
# print("Student object created")
# del s
# The __init__() method is a constructor and is called automatically when an object is created.
# The __del__() method is a destructor and is called when an object is deleted.
# In the program, s = Student() creates the object and calls the constructor.
# del s deletes the object and calls the destructor


# 2)inheritance:
# single inheritance:Single inheritance means a child class inherits properties and methods from only one parent class
# class Parent:
#     def show(self):
#         print("This is parent class")


# class Child(Parent):
#     def display(self):
#         print("This is child class")


# c = Child()
# c.show()
# c.display()
# Single inheritance means one child class inherits from one parent class.
# The child class can use the methods and variables of the parent class.
# In the program, Student inherits from Person.
# It helps in reusing the code of the parent class


# multiple inheritance:Multiple inheritance means a single child class inherits from two or more parent classes
# class Father:
#     def father(self):
#         print("Father class")


# class Mother:
#     def mother(self):
#         print("Mother class")


# class Child(Father, Mother):
#     def child(self):
#         print("Child class")


# c = Child()
# c.father()
# c.mother()
# c.child()
# Multiple inheritance means one child class inherits from two or more parent classes.
# The child class can access features of all its parent classes.
# For example, Child can inherit from both Father and Mother.
# This allows features from different classes to be combined.


# multilevel inheritace:Multilevel inheritance means inheritance occurs in multiple levels, where one class inherits from another and a third class inherits from the second
# class Grandfather:
#     def show1(self):
#         print("Grandfather")


# class Father(Grandfather):
#     def show2(self):
#         print("Father")


# class Son(Father):
#     def show3(self):
#         print("Son")


# s = Son()
# s.show1()
# s.show2()
# s.show3()
# Multilevel inheritance has inheritance in multiple levels.
# One class inherits from another class, and a third class inherits from the second.
# For example, Student inherits from Person, and Result inherits from Student.
# Thus, Result can access features of both Student and Person.

# public var function:Public members can be accessed directly from inside and outside the class.
# In Python, normal variables and functions are public by default
# class Student:
#     name = "Deva"

#     def show(self):
#         print(self.name)


# s = Student()
# print(s.name)
# s.show()
# Public members can be accessed inside and outside the class.
# In Python, variables and methods without _ or __ are normally public.
# The child class can directly access public members.
# They are easy to use and are commonly used when no access restriction is required.

# private var function:Private members are intended to be accessed only inside the class.
# In Python, we use __ before the variable or function name to make it private.
# class Student:
#     __name = "Deva"

#     def __show(self):
#         print(self.__name)

#     def display(self):
#         self.__show()


# s = Student()
# s.display()
# Private members are intended to be accessed only inside the class.
# They are written using double underscore (__).
# They cannot normally be accessed directly outside the class.
# Private members provide better data protection and hiding.

# protectd var function:Protected members are intended to be accessed inside the class and its child classes.
# In Python, we use a single _ before the variable or function name.
# class Parent:
#     _name = "Deva"

#     def _show(self):
#         print(self._name)


# class Child(Parent):
#     def display(self):
#         self._show()


# c = Child()
# c.display()
# Protected members are written using a single underscore (_).
# They are mainly intended to be used inside the class and its child classes.
# A child class can access protected members.
# Python does not strictly prevent outside access; _ mainly indicates that the member is protected by convention.


# hiericical inheritance:Hierarchical inheritance means multiple child classes inherit from the same parent class.
# class Parent:
#     def show(self):
#         print("Parent class")


# class Child1(Parent):
#     def display1(self):
#         print("Child 1")


# class Child2(Parent):
#     def display2(self):
#         print("Child 2")


# c1 = Child1()
# c1.show()
# c1.display1()

# c2 = Child2()
# c2.show()
# c2.display2()
# Hierarchical inheritance means multiple child classes inherit from one parent class.
# For example, Student and Teacher can both inherit from Person.
# Both child classes can use the common features of Person.
# It is useful when several classes need the same parent functionality


# hybrid inheritance:Hybrid inheritance is a combination of two or more types of inheritance.
# It can combine structures such as multiple, multilevel, and hierarchical inheritance
# class A:
#     def showA(self):
#         print("Class A")


# class B(A):
#     def showB(self):
#         print("Class B")


# class C(A):
#     def showC(self):
#         print("Class C")


# class D(B, C):
#     def showD(self):
#         print("Class D")


# d = D()
# d.showA()
# d.showB()
# d.showC()
# d.showD()
# Hybrid inheritance is a combination of two or more types of inheritance.
# It can combine single, multiple, multilevel, or hierarchical inheritance.
# For example, a program may use both hierarchical and multiple inheritance.
# It is useful for representing more complex relationships between classes.