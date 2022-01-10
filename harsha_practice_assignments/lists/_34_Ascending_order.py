l1=[4,3,2,6,5,8,9,10,12,54,23,22,11]

class Sorting_element:

    def __init__(self,list1):
        self.lst=list1


    def sorting_element(self):
        ls1=self.lst
        ls1.sort()
        print(ls1)

a=Sorting_element(l1)
a.sorting_element()