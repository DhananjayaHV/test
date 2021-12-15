class String_methods():

    def __init__(self):
        self.string1 = input("Enter the string : ")

    def Count_ch(self):
        # ch=input("Enter the character")
        ch_count = self.string1.count(f'{input("Enter the character")}')
        print("Total count of the characters", ch_count)

a=String_methods()
a.Count_ch()