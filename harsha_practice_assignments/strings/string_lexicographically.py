'''program to sort a string lexicographically'''
class A:
    def __init__(self):
        self.name = input("Enter the string : ")

    def my_func_lexSort(self):
        return print(sorted(sorted(self.name), key=str.lower))


a=A()
a.my_func_lexSort()
