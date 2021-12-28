import math

class Factorials():

    def __init__(self):
        self.input_number = int(input("Enter the number : "))

    def factorial_number(self):
        factorial_number = math.factorial(self.input_number)
        print("Factorial of the given number :",factorial_number)

a=Factorials()
a.factorial_number()
