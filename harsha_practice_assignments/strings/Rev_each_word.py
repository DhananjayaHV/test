class A:
    def __init__(self):
        self.strng=input("Enter the Sentance : ")
    def Rev_words(self):
        new_words= [word[::-1] for word in self.strng.split(" ")]
        print(" ".join(new_words))

a=A()
a.Rev_words()