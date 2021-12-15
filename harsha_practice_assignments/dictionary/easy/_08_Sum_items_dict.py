dic={'1':2,'2':3,'3':4}

class A:

    def __init__(self,dic1):
        self.dictnry1=dic1



    def Sum_dict(self):
        sum_value=sum(self.dictnry1.values())
        print("Total sum of the values in dict : ",sum_value)


a=A(dic)
a.Sum_dict()
