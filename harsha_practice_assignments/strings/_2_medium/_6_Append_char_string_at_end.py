class String_append:
    def __init__(self):
        self.strng=input("Enter the string : ")

    def appended(self):
        print("Your string is :",self.strng)
        edit=input('do you want to edit your string?..Y/N').lower()
        if edit=='y':
            self.strng=self.strng+" "+input("Enter here : ")
        print(self.strng)


a=String_append()
a.appended()
    # edited=str1+" "+input('enter : ')
    # print(edited)

