input_string = input('Enter elements of a list separated by space ')

def Even_odd(input_string):
    user_list = input_string.split()
    print('list: ', user_list)
    even=[]
    odd=[]


    for i in user_list:
        if int(i)%2==0:
            even.append(int(i))
        else:
            odd.append(int(i))


    print("Even numbers : ",even)
    print("Odd numbers : ",odd)

Even_odd(input_string)