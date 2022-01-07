def decor1(func):
    def inner_function():
        number1=func()
        if number1%2==0:
            # print(number)
            print("Decorator 1 is working fine...")
        else:
            print("The given number is odd number....")
        return number1
    return inner_function


def decor2(func):
    def inner():
        number=func()
        # while number>=5:
        try:
            if number>=5:
                if number%5==0:
                    print("Printing 2nd decorator....")
                else:
                    print('Given number is not a multiple of 5')
            else:
                raise Exception

        except:
            print("Please enter the number greater than 5 : ")
            inner()

    return inner


# @decor1
@decor2
def even_number():
    user_number=[]
    try:
        user_number = int(input("Enter the number : "))
    except ValueError as e:
        print("Please enter the valid number : ",e)

    return user_number


print(even_number())