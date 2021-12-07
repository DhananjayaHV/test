
class A:
    def __init__(self):
        set1=[]
        for i in range(int(input("Enter the length of set : "))):
            set1.append(input("Enter the set value : "))
        self.sets=set(set1)
        print(self.sets)

a =A()
a