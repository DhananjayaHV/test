cars = {'A':{'speed':70,'color':2},'B':{'speed':60,'color':3}}

class A:

    def __init__(self,dic):
        self.dic1=dic

    def dict_lne(self):
        for i in self.dic1:
            print(i)
            for k in self.dic1[i]:
                print(k,":",self.dic1[i][k])


a=A(cars)
a.dict_lne()