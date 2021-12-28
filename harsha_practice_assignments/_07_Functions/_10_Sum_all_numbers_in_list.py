class Sum_list():

    list_length = int(input("Enter the length of the list : "))

    def sum_list(self):
        list_numbers = []
        for i in range(Sum_list.list_length):
            number = int(input("Enter the number : "))
            list_numbers.append(number)
        print(list_numbers)
        print("Total sum of list", sum(list_numbers))

a=Sum_list()
a.sum_list()