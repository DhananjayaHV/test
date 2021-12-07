'''Count no of strings whose length is 2'''

class A:
    def __init__(self):
        self.strng=input("Enter the string : ")
        # print(self.strng)

    def String_length(self):
        counter=0
        for word in self.strng.split(" "):
            if len(word)==2:
                counter+=1
            else:
                pass
        print(f"There are {counter} strings whose length is 2.")



a =A()
a.String_length()