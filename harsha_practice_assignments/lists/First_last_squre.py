''''First,Last elements whose square value is between 1 and 30'''
class A:
    lst = [5, 6, 7, 2, 3, 4]
    def __init__(self):
        lst=[]
        for i in range(int(input("Enter the length of list : "))):
            lst.append(int(input("Enter the number : ")))
        self.list1 = lst


    def Square(self):
        lst2=[]
        for i in self.list1:
            if (i*i)<30:
                lst2.append(i)
            else:
                pass

        print("First element : ",min(lst2))
        print("Last element  : ",max(lst2))


a=A()
a.Square()