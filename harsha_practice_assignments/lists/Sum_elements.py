'''Sum of elements'''

class A:
    def __init__(self):
        list1=[]
        for i in range(int(input("Enter the length of list : "))):
            list1.append(int(input('Enter the number : ')))
        print("Entered list is : ",list1)
        self.lst1=list1
        self.sum_lsit=sum(self.lst1)
        print("Sum of elements in the list : ",self.sum_lsit)
a=A()
a