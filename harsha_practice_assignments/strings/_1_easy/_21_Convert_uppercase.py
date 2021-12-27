msg="Data preprocessing is an important task in text classification"

class A:

    def __init__(self,msg):
        self.msg=msg

    def upper(self):
        res=self.msg.upper()
        print("Sting in upper case: ",res)

a=A(msg)
a.upper()