input_string = input("Enter the string : ")
print("Input string is : ",input_string)
upper=[]
lower=[]
for i in input_string:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)

print("Lenght of upper case letters : ",len(upper))
print("Lenght of lower case letters",len(lower))