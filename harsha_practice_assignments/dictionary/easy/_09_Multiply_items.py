dic={'1':2,'2':3,'3':7}

class A:

    def __init__(self,dic1):
        self.dictnry1=dic1


    def Dict_multiply(self):
        product=1
        for i in self.dictnry1.values():
            product*=i
        print("Total sum of the values in dict : ",product)


a=A(dic)
a.Dict_multiply()
