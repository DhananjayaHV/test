from collections import OrderedDict
class A:
    def __init__(self):
        self.strng=input("Enter the string : ")

    def removeDup(self):
        return "".join(OrderedDict.fromkeys(self.strng))


a=A()
print(a.removeDup())

