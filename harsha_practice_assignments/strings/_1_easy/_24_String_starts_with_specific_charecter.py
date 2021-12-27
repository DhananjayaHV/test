msgs="What are you doing"

class A:

    def  __init__(self,msg):
        self.msg=msg

    def func1(self):
        valid=self.msg.startswith(input("Enter the chrecter"))
        print(valid)

a=A(msgs)
a.func1()