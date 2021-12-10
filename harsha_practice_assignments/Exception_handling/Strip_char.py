'''strip a set of characters from a string'''

class A:
    def __init__(self):
        self.strng=input("Enter the string : ")

    def Digit_letters_cal(self):
        digits = []
        letters=[]
        for i in self.strng:
            if i.isnumeric():
                digits.append(int(i))
            else:
                letters.append(i)

        try:
            print("Sum of digits in the string :", sum(digits))
            print("Sum of letters in the string :", sum(letters))
        except TypeError as e:
            print("Enter the value again",e)

a = A()
a.Digit_letters_cal()

