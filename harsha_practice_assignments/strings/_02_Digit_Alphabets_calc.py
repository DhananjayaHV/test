class A:
    def __init__(self,strng):
        self.strng=strng

    def Digit_letters_cal(self):
        letter = 0
        digits = 0
        sp = 0
        for i in self.strng:
            if str(i).isalpha():
                letter +=1
            elif str(i).isnumeric():
                digits +=1
            else:
                sp+=1

        print("Total letters found :", letter)
        print("Total digits found :", digits)
        print("Total Special characters  found :", sp)


a = A("jaha12345@#$")
a.Digit_letters_cal()




