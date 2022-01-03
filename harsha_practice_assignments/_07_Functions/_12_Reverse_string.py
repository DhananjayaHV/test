'''to reverse a string'''

class Reverse:

    def __init__(self):
        self.string=input("Enter the string :")

    def reversre_string(self):
        res=''
        for i in (list(reversed(self.string))):
            try:
                if i.isalpha():
                    res+=i
                else:
                    raise Exception
            except Exception as e:
                print(e)


        print("Reversed :",res)



a=Reverse()
a.reversre_string()

