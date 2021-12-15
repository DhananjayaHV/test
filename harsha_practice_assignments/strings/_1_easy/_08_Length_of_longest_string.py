'''Length of longest string in python'''
class A:
    def __init__(self):
        self.stng=input("Enter the string : ")

    def Length_string(self):
        max_len=0
        for word in self.stng.split(" "):
            if len(word)>max_len:
                max_len=len(word)
                self.word=word
        print("The longest string is : ",self.word)


a=A()
a.Length_string()