import sympy

class Prime_number():
    start = int(input("Enter the start range : "))
    end = int(input("Enter the end range : "))

    def Isprime(self):
        prime = []
        for i in range(Prime_number.start,Prime_number.end + 1):
            if sympy.isprime(i):
                prime.append(i)
            else:
                pass
        print(prime)

a=Prime_number()
a.Isprime()
