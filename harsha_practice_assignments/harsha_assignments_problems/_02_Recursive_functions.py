'''Recursive function'''
'''
Recursive Functions

A function that calls itself is known as Recursive Function.

Eg:

factorial(3)=3*factorial(2)
=3*2*factorial(1)
=3*2*1*factorial(0)
=3*2*1*1
=6

factorial(n)= n*factorial(n-1)

The main advantages of recursive functions are:
1. We can reduce length of the code and improves readability
2. We can solve complex problems very easily.

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

res=fact(4)
print(res)


lambda Function:
We can define by using lambda keyword
lambda n:n*n

res=lambda n:n*n
print(res(3))

numb=[i for i in range(1,50)]
print(numb)
even_numbers=[lambda i:i%2==0]
print(even_numbers(numb))

def eeven(num):
    for i in num:
        if i%2==0:
            print(i)
#
f= lambda n:n*n
v=f(3)
print(v)

su = lambda a,b:a if a>b else b
print(su(3,2))

num=[1,2,3,4,4,5,6,7,8]

res=list(map(lambda n:n*2,num))
print(res)



def num():
    yield 'a'
    yield 'b'
    yield 'c'

# a=num()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def myfunc(x,y):
    while x<=y:
        yield x
        x+=1

g=myfunc(10,20)

for i in g:
    print(i,end=" ")
'''

# input n

# n = 5
# # iterarte upto n
# for i in range(n):
#     print(' ' * (n - i), end='*')
#     print(' '.join(map(str,str(11 ** i))),end="*\n")
# n=8
#
# for i in range(n):
#     print(" "*(n-i),end="")
#     for j in range(i+1):
#         print('*',end=' ')
#
#     print('\r')

# a=[[0,1,2],[7,8,9],[4,5,6]]
# print([x for y in a for x in y])
# a,b,c,e,f='dhanu'
# print(type(a))
# # b,c='34'
# print(a,b,c,e,f)


# a,b=1>2,2>3
# lst=[a,b,a==b]
# print(lst)


# lst1=[1,2,3]
# lst2=[1,2,3]
# print(lst1==lst2)




a=[]
x=a.append(4)
y=a.append(60)
print(x)
# a.append()
print(a)