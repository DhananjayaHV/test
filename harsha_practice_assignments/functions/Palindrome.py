input_string = input("Enter  numbers separated by comma : ")
family_list  =int( input_string.split(","))
print(family_list)
def Palindrome(words):
    words_rev=words[::-1]
    print("The reversed word is : ", words_rev)
    if(words==words_rev):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")

# a = Palindrome(words)