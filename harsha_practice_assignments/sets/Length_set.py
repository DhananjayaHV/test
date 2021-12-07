'''Find the length of a set'''
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3,5,6,4}
C = {1, 2, 3}

class A:

    def __init__(self,set1):
        self.set1=set1

    def Length_set(self):
        return print("Length of dictionary is : ",len(self.set1))


a=A(setA)
a.Length_set()


