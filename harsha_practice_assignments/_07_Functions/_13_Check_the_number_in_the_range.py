class Range:

    def __init__(self):
        self.range1=int(input("Enter the start range :"))
        self.range2 = int(input("Enter the end range :"))
        self.number=int(input("Enter the number :"))

    def check_number_range(self):
        try:
            if self.range1 <= self.number <=self.range2  :
                print("Successful")
            else:
                raise Exception
        except ValueError as e:
            print("Please enter the valid number ",e)

#a=Range()
#a.check_number_range()


def check():
 while True:

    lr = int(input("Enter lower range : "))
    ur = int(input("Enter upper range : "))
    n = int(input("Enter no to check in between or not : "))

    try:
        if lr.isnumeric() and ur.isnumeric() and n.isnumeric():
            if lr<= n <=ur:
                print("Number is in the given range")
                break
            else:
                print("Entred number is not in the range")

        else:
            raise Exception
    except:
        print("Enter valid no")
    else:
        print("Enter again")
        return check()
        break
check()