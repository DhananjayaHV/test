msg="Data\npreprocessing\nis\nan\nimportant\ntask\nin\ntext\nclassification"

class A:

    def __init__(self,msg):
        self.msg=msg

    def remove_newline(self):
        new_msg=self.msg.replace("\n"," ")
        print(new_msg)

a=A(msg)
a.remove_newline()