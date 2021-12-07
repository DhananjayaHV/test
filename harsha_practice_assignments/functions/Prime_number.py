import sympy

start = int(input("Enter the upper range : "))
end = int(input("Enter the lower rangw : "))
def Isprime(start,end):
    prime=[]
    for i in range(start, end + 1):
        if sympy.isprime(i):
            prime.append(i)
        else:
            pass
    print(prime)

Isprime(start,end)