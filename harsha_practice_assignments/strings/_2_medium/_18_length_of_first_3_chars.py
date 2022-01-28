# str1=input('Enter the string :')

# if len(str1[0:3]) >3:
#     print(str1)
# else:
#     print(str1[0:3])


def func(str1):
    return str1[0:3] if len(str1)>3 else str1

print(func('hd'))