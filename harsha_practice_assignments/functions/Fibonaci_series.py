fb_length=int(input("Enter the range of FBS : "))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))



if fb_length <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(fb_length):
       print(recur_fibo(i))