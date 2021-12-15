msg="Data preprocessing is an important task in text classification"

class A:

    def __init__(self,msg):
        self.msg=msg

    def Lower_upper(self):
        res=self.msg.upper()
        print("Sting in upper case: ",res)
        res_lower=self.msg.lower()
        print("Sting in lower case: ", res_lower)

a=A(msg)
a.Lower_upper()