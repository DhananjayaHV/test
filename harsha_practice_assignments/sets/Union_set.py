'''Create a union of sets'''
set1 = {2, 3, 5}
set2 = {1, 3, 5}

class A:
    def __init__(self,set1,set2):
        self.set1=set1
        self.set2=set2

    def Union_set(self):
        print('Union set ',self.set1.union(self.set2))

a = A(set1,set2)
a.Union_set()