class Match:

    def __init__(self):

        self.dict1= {'key1': 1, 'key2': 3, 'key3': 2}
        self.dict2= {'key1': 1, 'key2': 3}

    def dict_matching(self):
        try:
            x,y=self.dict1,self.dict2
            for (key, value) in set(x.items()) & set(y.items()):
                print('%s: %s is present in both x and y' % (key, value))
        except Exception as e:
            print("Error!",e)


a=Match()
a.dict_matching()