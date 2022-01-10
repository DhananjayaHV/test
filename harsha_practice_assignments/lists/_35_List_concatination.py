class Create_list:

    def __init__(self):
        self.length=int(input("Enter the range : "))


    def create_list(self):
        lst=[i for i in range(0,self.length+1)]
        return lst


a=Create_list()
print(a.create_list())