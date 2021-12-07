list_length=int(input("Enter the length of the list : "))

def Mul_list(list_length):
    list_numbers=[]
    resul =1
    for i in range(list_length):
        number=int(input("Enter the number : "))
        list_numbers.append(number)
    for i in list_numbers:
        resul = i*resul
    print("Product of all the numbers in the list : ",resul)


Mul_list(list_length)