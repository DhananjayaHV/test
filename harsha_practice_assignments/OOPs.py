'''
OOPs
====

1) In python everything is an object and we need one blue print or model to create that object this model is nothing but class
2) We can write a class to represent the properties(attributes) and action (behaviour) of th object.
3) Properties ---Values
== actions - methods
=> Class containd both variables and methods

:keyword ===Class KeyValue

Syntax:
======

Class classNames
    "DOcstring"
    variable: instance variable,static variable and local variable
    methods: instance,static and class methods


Doc strting===  classname.__doc__

help(classname)


Within the Python class we can represent data by using variables.
There are 3 types of variables are allowed.

1. Instance Variables (Object Level Variables)
2. Static Variables (Class Level Variables)
3. Local variables (Method Level Variables)

Within the Python class, we can represent operations by using methods. The following are various
types of allowed methods


1. Instance Methods
2. Class Methods
3. Static Methods
'''
# Example for class:
# 1) class Student:
#
# 3) def __init__(self):
# 4) self.name='durga'
# 5) self.age=40
# 6) self.marks=80
# 7)
# 8) def talk(self):
# 9) print("Hello I am :",self.name)
# 10) print("My Age is:",self.age)
# 11) print("My Marks are:",self.marks)

'''
What is Object:
Pysical existence of a class is nothing but object. We can create any number of objects for a class.
Syntax to create object: referencevariable = classname()
Example: s = Student()

What is Reference Variable:
The variable which can be used to refer object is called reference variable.
By using reference variable, we can access properties and methods of object.

Program: Write a Python program to create a Student class and Creates an object to it. Call the
method talk() to display student details
'''
'''
class Student():
    name=input('Enter student name :')
    grade=input('Enter your grade :')
    regnumbre=input('Enter your register number :')

    def __init__(self):
        self.name = Student.name
        self.grade=Student.grade
        self.regnumber=Student.regnumbre


    def talk(self):
        return f'Hi i am {self.name},reg number {self.regnumber} and my grade is {self.grade} '


student_details = Student()
print(student_details.talk())
'''
'''
Self variable:
self is the default variable which is always pointing to current object (like this keyword in Java)
By using self we can access instance variables and instance methods of object.

Note:
1. self should be first parameter inside constructor
def __init__(self):
2. self should be first parameter inside instance methods
def talk(self):


Constructor Concept:
☕ Constructor is a special method in python.
☕ The name of the constructor should be __init__(self)
☕ Constructor will be executed automatically at the time of object creation.
☕ The main purpose of constructor is to declare and initialize instance variables.
☕ Per object constructor will be exeucted only once.
☕ Constructor can take atleast one argument(atleast self)
☕ Constructor is optional and if we are not providing any constructor then python will provide
default constructor.

Differences between Methods and Constructors:
Method Constructor
1. Name of method can be any name 1. Constructor name should be always __init__
2. Method will be executed if we call that
method
2. Constructor will be executed automatically at
the time of object creation.
3. Per object, method can be called any number
of times.
3. Per object, Constructor will be executed only
once
4. Inside method we can write business logic
4. Inside Constructor we have to declare and
initialize instance variables

Types of Variables:
Inside Python class 3 types of variables are allowed.
1. Instance Variables (Object Level Variables)
2. Static Variables (Class Level Variables)
3. Local variables (Method Level Variables)


1. Instance Variables:

If the value of a variable is varied from object to object, then such type of variables are called
instance variables.

For every object a separate copy of instance variables will be created.

Where we can declare Instance variables:

1. Inside Constructor by using self variable
2. Inside Instance Method by using self variable
3. Outside of the class by using object reference variable

class Student():
    name=input('Enter student name :')
    grade=input('Enter your grade :')
    regnumbre=input('Enter your register number :')

    def __init__(self):
        self.name = Student.name
        self.grade=Student.grade
        self.regnumber=Student.regnumbre


    def talk(self):
        return f'Hi i am {self.name},reg number {self.regnumber} and my grade is {self.grade} '


student_details = Student()
dic=student_details.__dict__
print(dic)
print(student_details.talk())

2. Inside Instance Method by using self variable:
We can also declare instance variables inside instance method by using self variable. If any
instance variable declared inside instance method, that instance variable will be added once we
call that method.

3. Outside of the class by using object reference variable:
We can also add instance variables outside of a class to a particular object.

How to access Instance variables:
We can access instance variables with in the class by using self variable and outside of the class by
using object reference.

How to delete instance variable from the object:
1. Within a class we can delete instance variable as follows
del self.variableName
2. From outside of class we can delete instance variables as follows
del objectreference.variableName0

class a:

    def __init__(self):
        self.name=int(input("gg"))
        self.id=input('id')


ovj=a()
print(ovj.__dict__)

a='hai'*3

b=len
def length(a,b):
    # a.append(ob)
    print(b(a)*4)


length(a,b)



How to delete instance variable from the object:
1. Within a class we can delete instance variable as follows
del self.variableName
2. From outside of class we can delete instance variables as follows
del objectreference.variableName

class a:

    def __init__(self):
        self.f=10

    def meth(self):
        self.me=20
        # del self.f
        print(self.f)


a=a()
del a.f
a.meth()

print(a.me)

If we change the values of instance variables of one object then those changes won't be reflected
to the remaining objects, because for every object we are separate copy of instance variables are
available.

'''
