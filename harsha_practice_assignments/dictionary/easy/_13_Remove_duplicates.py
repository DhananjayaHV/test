dic={'1':30,'2':30,'3':7}

class A:

    def __init__(self,dict1):
        self.dict1=dict1

    def Rm_duplicates(self):
        result = {}
        for key,value in dic.items():
            if value not in result.values():
                result[key] = value
        print(result)



a=A(dic)
a.Rm_duplicates()