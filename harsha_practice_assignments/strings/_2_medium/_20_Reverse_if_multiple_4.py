str1=input('Enter :').split()
s=''
for w in str1:
    if len(w)==4:
        r=w[::-1]
        s+=' '+r
    else:
        s+=' '+w
print("Reversed string :",s)

