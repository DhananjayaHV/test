import numpy

list_lenght=int(input("Enter the length of list : "))
def Unique_num(list_lenght):
    lis=[]
    for i in range(list_lenght):
        list_elements=int(input("Enter the number : "))
        lis.append(list_elements)
    print(lis)

    uniquee=numpy.unique(lis)
    print(uniquee)

    set_list=set(lis)
    print("Unique list : ",list(set_list))

Unique_num(list_lenght)