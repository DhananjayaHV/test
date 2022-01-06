class Even_numbers:

    def __init__(self,lst):
        self.lis1=lst


    def even_number(self):
        even=[]
        odd=[]
        for i in self.lis1:
            try:
                if i%2==0:
                    even.append(i)
            except Exception:
                print("")

        return even

lsit1=[1,2,3,4,5,6,7,8,9,'a']
a=Even_numbers(lsit1)
print(a.even_number())