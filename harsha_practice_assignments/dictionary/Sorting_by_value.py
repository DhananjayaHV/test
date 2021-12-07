import operator
markdict = {"Tom": 670, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya": 73}

class A:

    def __init__(self,dic):
        self.dictry=dic

    def Sort_By_Value(self):
        marklist = sorted(self.dictry.items(), key=operator.itemgetter(1))
        sortdict = dict(marklist)
        print(sortdict)

a=A(markdict)
a.Sort_By_Value()