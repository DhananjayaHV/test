class Palindrome():

    def __init__(self):
        self.input_word = input("Enter word : ")


    def palindrome(self):
        words_rev=self.input_word[::-1]
        print("The reversed word is : ", words_rev)
        if(self.input_word==words_rev):
            print("The string is a palindrome")
        else:
            print("Not a palindrome")

a = Palindrome()
a.palindrome()