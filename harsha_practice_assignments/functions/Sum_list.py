list_length=int(input("Enter the length of the list : "))

def sum_list(list_length):
    list_numbers=[]
    for i in range(list_length):
        number=int(input("Enter the number : "))
        list_numbers.append(number)
    print(list_numbers)
    print("Total sum of list",sum(list_numbers))

sum_list(list_length)