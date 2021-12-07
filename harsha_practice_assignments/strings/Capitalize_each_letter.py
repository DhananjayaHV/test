'''capitalize first and last letters of each word of a given string'''

class A:
    def __init__(self):
        self.strng=input("Enter the sentance : ")

    def Capitaslizer(self):
        result=""
        for word in self.strng.split(" "):
            result+=word[0:-1].capitalize() + word[-1].upper()+" "
        print(result)

a = A()
a.Capitaslizer()
# a.Capitaslizer()