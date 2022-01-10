class Mul_intsing_int:

    def __init__(self,lst):
        self.intiger=lst


    def converting(self):
        lst=self.intiger
        res=[str(i) for i in lst]
        result=int(''.join(res))
        # print(result)
        return result

l=[1,2,3,4,5,6]
a=Mul_intsing_int(l)
print(a.converting())
# print(a)
#
# listA = [22,11,34]
# # # Given list
# # print("Given list A: ", listA)
# # # Use
# res = int("".join([str(i) for i in listA]))
# # # Result
# print("The integer is : ",res)
#
# # s = [str(i) for i in l]
# s=[]
# for i in l:
#     s.append(str(i))
#     print('Fater',''.join(s))
#     print(s)
# r = int("".join(s))
# # print(r)