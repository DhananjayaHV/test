dic={'name':"Bangaluru","location":"karnataka",'country':"India"}

class A:

    def __init__(self,dic):
        self.dictnry=dic


    def search_key(self):
        key=input("Enter key: ")
        if key in self.dictnry.keys():
            print("Key is present")
        else:
            print("Key not found")


a=A(dic)
a.search_key()
