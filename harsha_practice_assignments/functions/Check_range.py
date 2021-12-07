u_range=int(input("Enter the upper range : "))
l_range=int(input("Enter the lower range : "))
number=int(input("Enter the number : "))
if number  in range(u_range,l_range):
   print(f"Entered number {number} is in the range.")
else:
    print(f"Entered number {number} not in the range.")
