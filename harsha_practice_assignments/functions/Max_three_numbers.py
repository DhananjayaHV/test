def max_number():
    list_numbers=[]
    for i in range(1,4):
        user_input=int(input(f"Enter the {i}th number : "))
        list_numbers.append(user_input)
    print("List of numbers : ",list_numbers)

    max_number=max(list_numbers)
    return print("Max of three numbers",max_number)

max_number()