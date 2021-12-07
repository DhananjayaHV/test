
class A:
    def __init__(self):
        self.strng=input("Enter the string : ")

    def Digit_letters_cal(self):
        digits = []
        for i in self.strng:
            if str(i).isnumeric():
                digits.append(int(i))

        print("Sum of digits in the string :", sum(digits))

a = A()
a.Digit_letters_cal()

