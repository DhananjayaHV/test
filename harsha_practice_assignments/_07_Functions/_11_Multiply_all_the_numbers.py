'''multiply all the numbers in a list'''

class Multiply:

    def __init__(self,lst):
        self.lst=lst

    def multiply(self):
        try:
            result=1
            for i in self.lst:
                if type(i)==int:
                    result=result*i
                else:
                    raise Exception
            print("Result",result)
        except Exception as e:
            print("Error!.. Please use int",e)


list1=[1,2,4,'v']
a=Multiply(list1)
a.multiply()
