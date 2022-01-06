class Pascal:

    def __init__(self):
        self.number=int(input("Enter the number of rows:"))


    def pascals(self):
            n=self.number
            for i in range(n):
                print(' ' * (n - i), end='')
                print(' '.join(map(str, str(11 ** i))))


a=Pascal()
a.pascals()