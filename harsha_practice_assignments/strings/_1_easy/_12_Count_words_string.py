msg="Data preprocessing is an important task in text classification"

class A:

    def __init__(self,msg):
        self.msg=msg

    def words_count(self):
        counter=len(msg.split(" "))
        print("Total words in string : ",counter)


a=A(msg)
a.words_count()
