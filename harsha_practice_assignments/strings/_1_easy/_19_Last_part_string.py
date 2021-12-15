msg="Data preprocessing is an important task in text classification"

class A:

    def __init__(self,msg):
        self.msg=msg

    def last_part(self):
        for word in self.msg.split(" "):
            continue
        print(word)


a=A(msg)
a.last_part()