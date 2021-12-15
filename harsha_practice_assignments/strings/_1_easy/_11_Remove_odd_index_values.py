msg="HaiEmployee"

class A:

    def __init__(self,msg):
        self.msg=msg

    def Odd_index_remove(self):
        srng=""
        for i in range(len(self.msg)):
            if i%2==0:
                srng=srng+self.msg[i]
        print("String after removig the odd index values : ",srng)


a=A(msg)
a.Odd_index_remove()