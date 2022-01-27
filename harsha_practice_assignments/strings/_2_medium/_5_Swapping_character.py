str1='what are you doing'
str12=list(str1)
for i in range(0,len(str12)-1):
    str12[i],str12[i+1]=str12[i+1],str12[i]
    print(''.join(str12))


#
# for i in range(0,len(str1),2):
#     str1[i],str1[i+1] =str1[i+1],str1[i]
#     print(''.join(str1))

def solve(s):
   s = list(s)
   for i in range(0, len(s)-1, 2):
      s[i], s[i+1] = s[i+1], s[i]
   print(''.join(s))
   # return ''.join(s)

# s = "programming"
# print(solve(s))
