dic={'1':2,'2':30,'3':7}

class A:

    def __init__(self,dic1):
        self.dictnry1=dic1


    def Max_min_value(self):
        max_value=max(self.dictnry1.values())
        min_value=min(self.dictnry1.values())
        print("The maximum value is: ",max_value)
        print("The minimum value is: ", min_value)


a=A(dic)
a.Max_min_value()
