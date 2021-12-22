number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    print("digit ",digit)
    rev = (rev*10)+digit
    print("Rev ",rev)
    number = number//10
    print("Number ",number)
print(rev)