class Unique:

    def __init__(self,lst):
        self.list1=lst

    def unique_elements(self):
        x=[]
        for i in self.list1:
            try:
                if type(i) == int:
                        if i not in x:
                            x.append(i)
                        else:
                            continue
                else:
                    raise Exception

            except Exception as e:
                print("Error!..Found non int element ",i)

        return x

lis=[1,1,1,1,2,3,4,5,55,5,5,5,5,5,6,6,7,8,8,8,'a','b']
uni=Unique(lis)
print(uni.unique_elements())