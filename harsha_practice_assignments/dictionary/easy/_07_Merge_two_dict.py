dic1={'name':"Bangaluru","location":"karnataka",'country':"India"}
dic2={'1':2,'2':3,'3':4}
class A:

    def __init__(self,dic1,dict2):
        self.dictnry1=dic1
        self.dictnry2 = dict2


    def Merge(self):
        self.dictnry1.update(self.dictnry2)
        print(self.dictnry1)
        # z={**dic1,**dic2}


a=A(dic1,dic2)
a.Merge()
