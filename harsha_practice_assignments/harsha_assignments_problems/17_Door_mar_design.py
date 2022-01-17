class Door_mat:

    def __init__(self):
        self.n=int(input("Enter the number of rows : "))

    def pattern(self):
        n=self.n
        m=n*3
        for i in range(1,n,2):
            print((".|."*i).center(m,'*'))
        print("WELCOME".center(m,'*'))
        for j in range(n-2,-1,-2):
            print(('.|.'*j).center(m,'*'))


a=Door_mat()
a.pattern()
