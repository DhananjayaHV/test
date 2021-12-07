'''Sort a list alphabetically in a dictionary.'''
dict ={
    "L1": ["Tiger", "Lion", "Cat"],
    "L2": ["Man", "Computer", "B-science"],
    "L3": ["portal", "for", "Server"],
}
class A:

    def __init__(self):
        pass

    def Sort_list(self,dictnry):
        for i, j in dictnry.items():
            sorted_dict = {i: sorted(j)}
            print(sorted_dict)


a=A()
a.Sort_list(dict)