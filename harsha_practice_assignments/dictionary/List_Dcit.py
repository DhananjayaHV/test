from collections import defaultdict
lst1=['Apple','Mango','Orange','Tiger','Elephant']
lst2=[5,2,3,8,5]

class A:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2

    # def Dict_creator(self):
    #     res={self.list1[i]:self.list2[i] for i in range(len(self.list1))}
    #     print(res)


    def Dict_wold(self):
        temp = {}
        for c, i in zip(self.list1, self.list2):
            temp[c] = i
        print(temp)


a=A(lst1,lst2)
a.Dict_wold()

#
# dict_1={}
#
# for key,value in zip(lst1,lst2):
#     if key not in dict_1:
#         dict_1[key]=[value]
#     else:
#         dict_1[key].append(value)
#
# print(dict_1)