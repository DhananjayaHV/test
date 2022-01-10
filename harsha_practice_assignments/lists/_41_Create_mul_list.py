class Mul_list:

    def __init__(self):
        self.range1=int(input("Enter the range : "))

    def create_mul_list(self):
        dictionary={}
        n=self.range1
        for i in range(1,n+1):
            dictionary[i]=[]
        return dictionary


a=Mul_list()
print(a.create_mul_list())