'''FUNCTIONS'''

'''
If a group of statements is repeatedly required then it is not recommended to write these
statements everytime seperately.We have to define these statements as a single unit and
we can call that unit any number of times based on our requirement without rewriting.
This unit is nothing but function.

The main advantage of functions is code Reusability.
Note: In other languages functions are known as methods,procedures,subroutines etc


Python supports 2 types of functions
1. Built in Functions
2. User Defined Functions

1. Built in Functions:
The functions which are coming along with Python software automatically,are called built
in functions or pre defined functions

Eg:
id()
type()
input()
eval()
etc..

2. User Defined Functions:
The functions which are developed by programmer explicitly according to business
requirements ,are called user defined functions.


Syntax to create user defined functions:
def function_name(parameters) :
""" doc string"""
----
-----
return value



Note: While creating functions we can use 2 keywords
1. def (mandatory)
2. return (optional)

Eg 1: Write a function to print Hello
test.py:

def wish():
   print("Hello Good Morning")
   
wish()


Parameters
Parameters are inputs to the function. If a function contains parameters,then at the time
of calling,compulsory we should provide values otherwise,otherwise we will get error.

Eg: Write a function to take name of the student as input and print wish message by
name.

def name(stu_name):
    print(f'Hi {stu_name}')

name('dhananjay')


def square(x):
    # print("Square is : ",x**x)
    return f'Square is :{x**x}'
a=square(2)
print(a)


Return Statement:

Function can take input values as parameters and executes business logic, and returns
output to the caller with return statement.

Q. Write a function to accept 2 numbers as input and return sum.

def add(x,y):
    return x+y

a=add(2,3)
print("Sum :",a)

If we are not writing return statement then default return value is None.

def func():
    return "Dhananjay"

a=func
print(a())
print(func)

def func():
    print("Dhananjay")
    # return "Dhananjay"

a=func()
a
func()

# print(func())
# print(func)


def fac(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    print(res)

# fac(4)
num=4
res=1
while num>=1:
    res=res*num
    num-=1

print(res)



Returning multiple values from a function:

In other languages like C,C++ and Java, function can return atmost one value. But in
Python, a function can return any number of values.

def sum_diff(x,y):
        sum=x+y
        diff=x-y
        return sum,diff

a,c=sum_diff(12,5)
print(a)
print(sum_diff(12,5))

Types of arguments
===================

def f1(a,b):
------
------
------
f1(10,20)

a,b are formal arguments where as 10,20 are actual arguments

There are 4 types are actual arguments are allowed in Python.
1. positional arguments
2. keyword arguments
3. default arguments
4. Variable length arguments


1. positional arguments:

These are the arguments passed to function in correct positional order.
def sub(a,b):
print(a-b)
sub(100,200)
sub(200,100)

The number of arguments and position of arguments must be matched. If we change the
order then result may be changed.
If we change the number of arguments then we will get error.

2. keyword arguments:

We can pass argument values by keyword i.e by parameter name.

Eg:

def keyword(age,name):
    print(age,name)

keyword(name='dhanu',age=21)

Here the order of arguments is not important but number of arguments must be matched.

Note:
We can use both positional and keyword arguments simultaneously. But first we have to
take positional arguments and then keyword arguments,otherwise we will get
syntaxerror.

3. Default Arguments:
Sometimes we can provide default values for our positional arguments.

def wish(name="Guest"):
   print("Hello",name,"Good Morning")

wish()
wish("Dhanu)

***Note:
After default arguments we should not take non default arguments
def wish(name="Guest",msg="Good Morning"): ===>Valid
def wish(name,msg="Good Morning"): ===>Valid
def wish(name="Guest",msg): ==>Invalid
SyntaxError: non-default argument follows default argument.

4. Variable length arguments:

Sometimes we can pass variable number of arguments to our function,such type of
arguments are called variable length arguments.

We can declare a variable length argument with * symbol as follows

def f1(*n):

We can call this function by passing any number of arguments including zero number.
Internally all these values represented in the form of tuple.

def func(*n):
    sumb=0
    for n1 in n:
        sumb=sumb+n1
    print(sumb)

func(1,2,4)

Note:
We can mix variable length arguments with positional arguments.

def f1(n1,*s):
   print(n1)
   for s1 in s:
   print(s1)

 f1(10)
 f1(10,20,30,40)
 f1(10,"A",30,"B")


def num(n,*nm):
    summ=n+1
    mul=1
    for i in nm:
        mul=mul*i
    print('sum',summ)
    print("mul",mul)

num(2,3,2)

Note: After variable length argument,if we are taking any other arguments then we
should provide values as keyword arguments.

def f1(*s,n1):
2) for s1 in s:
3) print(s1)
4) print(n1)
5)
6) f1("A","B",n1=10)
7) Output
8) A
9) B
10) 10


f1("A","B",10) ==>Invalid
TypeError: f1() missing 1 required keyword-only argument: 'n1'

Note: We can declare key word variable length arguments also.
For this we have to use **.
def f1(**n):
We can call this function by passing any number of keyword arguments. Internally these
keyword arguments will be stored inside a dictionary.

1) def display(**kwargs):
2) for k,v in kwargs.items():
3) print(k,"=",v)
4) display(n1=10,n2=20,n3=30)
5) display(rno=100,name="Durga",marks=70,subject="Java")

def func(**kwrgs):
    for k,v in kwrgs.items():
        print(k,v)

func(a=10,b=20,c=23)


Types of Variables
========================

Python supports 2 types of variables.

1. Global Variables
2. Local Variables

1. Global Variables
===================
The variables which are declared outside of function are called global variables.
These variables can be accessed in all functions of that module.

a=10 # global variable
def f1():
 print(a)
 
2. Local Variables:
===================

The variables which are declared inside a function are called local variables.
Local variables are available only for the function in which we declared it.i.e from outside
of function we cannot access.

a=10
# print(a)
def funv():
    # global a
    a=88
    print("global",globals()['a'])
    print(a)

funv()
print(a)


Recursive Functions
===================

A function that calls itself is known as Recursive Function.

1. We can reduce length of the code and improves readability
2. We can solve complex problems very easily.

Anonymous Functions:
Sometimes we can declare a function without any name,such type of nameless functions
are called anonymous functions or lambda functions.
The main purpose of anonymous function is just for instant use(i.e for one time usage)

Normal Function:

We can define by using def keyword.

def squareIt(n):
return n*n


lambda Function:
We can define by using lambda keyword
lambda n:n*n

n=lambda a:a*a
print(n(2))

s=lambda a,b:a+b
print(s(2,4))


Note:
Lambda Function internally returns expression value and we are not required to write
return statement explicitly.

Note: Sometimes we can pass function as argument to another function. In such cases
lambda functions are best choice.

We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z
these functions expect function as argument.

Decorators:
==========



def swap(func):

    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner



@swap
def div(a,b):
    return a/b

print(div(2,4))


def smart(func):

    def inner(name):
        if name=="dhanu":
             print('hi dhananjay')
        else:
            func(name)
    return inner

@smart
def wish(name):
    print('max')

a=wish('dhanu1')
print(a)


Decorator Chaining
===================
We can define multiple decorators for the same function and all these decorators will
form Decorator Chaining.

Eg:
@decor1
@decor
def num():

For num() function we are applying 2 decorator functions. First inner decorator will work
and then outer decorator.


def func1(func):

    def inner():
        print("Hello")
        func()
    return inner()

def func2(func):

    def inner():
        print("Second decorator")
        func()
    return inner

@func2
@func1
def num():
    return "dhanu"

print(num)



def decor(func):
    def inner(x):
        value=func(x)
        print("dec1",value)
        if value%2==0:
            # a=value+1
            pass
        return value+1
    return inner

def decor1(func):
    def inner(x):
        value=func(x)
        print(value)
        if value%2==1:
            print("Not completed")
        else:
            print("value")
        return value+1
    return inner


@decor1
@decor
def num(x):
    print("My function")
    # print("hello")
    x+=1
    return x


print(num(4))



'''
def smart(fun):
    def inner(a,b):
        if a%2==0 and b%2==0:
            a=fun(a,b)
        else:
            print("Not even numbers")
        return a
    return inner


@smart
def add(x,y):
    return x+y

# print(add(2,4))



def decor(func):
    def inner(x):
        value=func(x)
        print("dec1",value)
        if value%2==0:
            # a=value+1
            pass
        return f'decor1 output {value + 1}'
    return inner

def decor1(func):
    def inner1(x):
        value=func(x)
        print(value)
        if value%2==1:
            print("Not completed")
        else:
            print("value")
        return value+1
    return inner1


@decor1
@decor
def num(x):
    print("My function")
    # print("hello")
    x+=1
    return x


print(num(4))
