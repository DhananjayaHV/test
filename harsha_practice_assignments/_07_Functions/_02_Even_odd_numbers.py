class Even_Odd():

    input_string = input('Enter elements of a list separated by space ')
    def __init__(self):
        pass

    def Even_odd(self):
        user_list = Even_Odd.input_string.split()
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

a=Even_Odd()
a.Even_odd()