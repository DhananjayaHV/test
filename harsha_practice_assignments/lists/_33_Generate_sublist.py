from itertools import combinations

class Sublist:

    def __init__(self,lst):
        self.my_list=lst

    def sub_lists(self):
        my_list=self.my_list
        subs = []

        temp =[ [list(j) for j in combinations(my_list, i)] for i in range(0, len(my_list)+1)]
        if len(temp)>0:
            subs.extend(temp)
        return subs




l1 = [10, 20, 30, 40]
a=Sublist(l1)
print(a.sub_lists())
