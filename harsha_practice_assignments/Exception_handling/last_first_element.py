'''First,Last elements whose square value is between 1 and 30'''
list1=[]
for j in range(int(input("Enter the length of the list : "))):
    list1.append(input("Enter the naumber"))
    print(list1)

list2=[]
for i in list1:
    try:
        if (int(i)*int(i))<30:
            list2.append(int(i))
    except:
        print("Enter valid number in place of ",i)

print("First element is : ",min(list2))
print("last element is : ",max(list2))
