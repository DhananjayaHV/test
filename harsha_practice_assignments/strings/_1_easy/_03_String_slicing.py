class String_methods():

    def __init__(self):
        self.string1=input("Enter the string : ")

    def String_Slicing(self):
        sliced_string=self.string1[int(input("Enter the start point : ")):int(input("Enter the end point : "))]
        print("String after slicing : ",sliced_string)



a=String_methods()
a.String_Slicing()