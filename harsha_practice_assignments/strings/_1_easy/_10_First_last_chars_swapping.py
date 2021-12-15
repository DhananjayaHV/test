

msg='Hai Bengaluru'

class A:
    def __init__(self,msg):
        self.msg=msg

    def swap(self):
        new_stng=self.msg[-1]+self.msg[1:-1]+self.msg[:1]
        print("String after swapping : ",new_stng)


a=A(msg)
a.swap()
