
lst1=[1,2,3]
lst2=[3,4,5]

# print(set(lst1) | set(lst2))
# print(res)

# a=2
# b=4
# print(a & b)
class Common_items:

    def __init__(self,l1,l2):
        self.lst1=l1
        self.lst2=l2

    def common_elements(self):
        l1=self.lst1
        l2=self.lst2
        return set(l1) & set(l2)


a=Common_items(lst1,lst2)
print(a.common_elements())