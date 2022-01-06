class A:

    def __init__(self):
        self.string= input("Enter the string : ")


    def upper_lower(self):
        input_string=self.string
        upper = []
        lower = []
        print("Input string is : ", input_string)
        for i in input_string:
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)

        print("Lenght of upper case letters : ", len(upper))
        print("Lenght of lower case letters", len(lower))

a=A()
a.upper_lower()