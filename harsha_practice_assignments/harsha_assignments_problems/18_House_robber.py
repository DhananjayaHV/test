
lst=[]

maxi=0
num1=0
num2=0
for i in range(len(lst)-2):
    res=(lst[i]+lst[i+2])
    if res>maxi:
        maxi=res
        num1=lst[i]
        num2=lst[i+2]

print(num1,num2)
print(maxi)


# print(rob(lst))