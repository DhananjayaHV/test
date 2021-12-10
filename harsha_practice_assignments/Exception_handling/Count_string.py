'''Count no of strings whose length is 2'''

class A:
    def __init__(self):
        self.strng=input("Enter the string : ")
        # print(self.strng)

    def String_length(self):
        counter=0
        try:
            for word in self.strng.split(" "):
                if len(word)==2:
                    counter+=1
                    print(f"There are {counter} strings whose length is 2.")
                    raise NameError
                else:
                    pass

        except NameError as n:
            print("Erro5",n)



a =A()
a.String_length()