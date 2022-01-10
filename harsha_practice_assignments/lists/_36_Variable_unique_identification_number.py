'''Variable unique identification number'''

class UID:

    def __init__(self):
        self.number=lst1

    def UID_number(self):
        res=[id(i) for i in self.number]
        print(res)



lst1=[1,2,3,4]
a=UID()
a.UID_number()