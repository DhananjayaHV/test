class A:

    def __init__(self):
        pass



    def key_add(self):
        dic={}
        for i in range(int(input("Enter the numbers of items you want to add : "))):
            key_name=input("Enter the key : ")
            key_value=input("Enter the corresponding value : ")
            dic[key_name]=key_value
        print(dic)


a=A()
a.key_add()