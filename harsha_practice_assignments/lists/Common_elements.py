lst1=[1,2,3,4,5,6,7,8]
lst2=[1,34,4,5,7,8]
class A:

    def __init__(self,lst1,lst2):
        self.lst1=lst1
        self.lst2=lst2

    def Sort_list(self):
        return  print(list(set(self.lst1).intersection(self.lst2)))

a =A(lst1,lst2)
a.Sort_list()
