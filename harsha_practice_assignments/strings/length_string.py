class String_methods():

    def __init__(self):
        self.string1=input("Enter the string : ")

    def length1(self):
        # print("Length of the string : ", len(self.string1))
        return print("Length of the string : ",len(self.string1))

    def Count_ch(self):
        # ch=input("Enter the character")
        ch_count=self.string1.count(f'{input("Enter the character")}')
        print("Total count of the characters",ch_count)
        # return ch_count

    def String_Slicing(self):
        sliced_string=self.string1[int(input("Enter the start point : ")):int(input("Enter the end point : "))]
        print("String after slicing : ",sliced_string)

    def String_replace(self):
        stg_replace=self.string1.replace(input("Enter the string to replace : "),input("Enter the string to be replace : "),int(input('Enter the count : ')))
        return print("Replaced string : ",stg_replace)

    def swap(self):
        c = list(self.string1)
        i=int(input('Enter index of first the character to swap :'))
        j=int(input('Enter index of second the character to swap :'))
        c[i], c[j] = c[j], c[i]
        return print(''.join(c))


    def Append_character(self):
        res=self.string1+input("Enter the string to append :")
        print(res)

a= String_methods()
a.Append_character()
