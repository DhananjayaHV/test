user_input=int(input("Enter the number : "))

def table_calculatore(user_input):
    for i in range(1,11):
        result = user_input*i
        print(f'{user_input} X {i} = {result}')

table_calculatore(user_input)