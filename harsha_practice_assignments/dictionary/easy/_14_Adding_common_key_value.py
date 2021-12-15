dict1 = {'a': 12, 'for': 25, 'm': 9}
dict2 = {'a': 100, 'b': 200, 'm': 300}

class A:

    def __init__(self,dic1,dic2):
        self.dict1=dic1
        self.dict2=dic2

    def Add_dictionary_value(self):
        for key,value in self.dict2.items():
            if key in self.dict1:
                self.dict1[key] = self.dict2[key] + self.dict1[key]
            else:
                self.dict1[key]=value
        print(dict1)

a=A(dict1,dict2)
a.Add_dictionary_value()