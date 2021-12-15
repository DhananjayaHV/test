# 0. Mathematics
'''
1.Import the given string.
2.iterate each character and increment the counter.
3.print the counter as final length.
'''

# 1.Builtin functions
print("*****1. Built Functions*******")

strng='Hi Bengaluru'
print("Length of the string is : ",len(strng))

#2. Algorithm

print("--------2. Algorithm----------")

strng='Hi Bengaluru'

counter=0
for i in strng:
    counter+=1
print("Length of the string is : ",counter)

#3. USing funcions

print("--------3 Using Functions----------")

#State
msg="Hai Bengaluru"

#Behaviour
def str_len(strng):
    counter = 0
    for i in strng:
        counter += 1
    print("Length of the string is : ", counter)

str_len(msg)

# With return type
print("********Using return type********")
def str_len(strng):
    counter = 0
    for i in strng:
        counter += 1
    return counter
total_length=str_len(msg)
print("Total length of the string is : ",total_length)

#OOPs
print("-----using oops-----")

msg1="Hai bengaluru"

class A:

    def __init__(self,msg1):
        self.msg=msg1

    def str_len(self):
        counter = 0
        for i in self.msg:
            counter += 1
        return counter

abj=A(msg1)
length=abj.str_len()
print("Total length is : ",length)


