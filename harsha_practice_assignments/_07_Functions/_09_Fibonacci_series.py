class Fibonacci():

    def __init__(self):
        self.fb_length = int(input("Enter the range of FBS : "))

    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return Fibonacci.recur_fibo(n - 1) + Fibonacci.recur_fibo(n - 2)
    def check(self):
        if self.fb_length <= 0:
            print("Plese enter a positive integer")
        else:
            print("Fibonacci sequence:")
            for i in range(self.fb_length):
                print(Fibonacci.recur_fibo(i))

f=Fibonacci()
f.check()
