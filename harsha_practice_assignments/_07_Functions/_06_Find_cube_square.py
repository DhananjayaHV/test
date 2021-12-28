class Cube_square():

    def __init__(self):
        self.user_input = int(input("Enter the number : "))



    def Square(self):
        return print("Square of the given number is : ",self.user_input * self.user_input)

    def Cube(self):
        return print("Cube of the given number is : ",self.user_input * self.user_input * self.user_input)


a=Cube_square()
a.Cube()
a.Square()
