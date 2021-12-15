msg='dhananjaya'

class A:

    def __init__(self,strg):
        self.dict1=strg

    def String_dict(self):
        dict1={}
        for i in msg:
            dict1[i]=dict1.get(i,0)+1
        print(dict1)

#
# a=A(msg)
# a.String_dict()

dict = {"a":1,"b":2,"a":3}
dict["a"]=4
print(dict)

dict = {}
string = "aabcdea"
for i in string:
    dict[i]=dict.get(i,0)+1
print("New dict",dict)

