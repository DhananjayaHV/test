'''Need to chech this pgm'''

class A:
    def __init__(self):
        self.strng=input("Enter the Sentance : ")
    def Rev_words(self):
        rev_strng = self.strng[::-1]
        print("Reversed string :",rev_strng)
        new_words= [word[::-1] for word in rev_strng.split(" ")]
        new_list=" ".join(new_words)
        print(new_list)
a=A()
a.Rev_words()