'''Finding a second largest number'''

class A:
    def __init__(self):
        list1=[]
        for i in range(int(input("Enter the length of list : "))):
            list1.append(int(input('Enter the number : ')))
        print("Entered list is : ",list1)
        self.lst1=list1
        self.sorted=sorted(self.lst1)
        # print("Sorted list : ",self.sorted)
        print("Second largest number is : ", self.sorted[-2])
a=A()
a