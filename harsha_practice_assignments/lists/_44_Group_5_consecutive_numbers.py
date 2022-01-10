


number_list=[i for i in range(1,100)]
# print(number_list)
l = [[5*i + j for j in range(1,6)] for i in range(15)]
print(l)
mainn=[]
res=[]
for i in range(100):
    res.append(i)

for j in range(0,len(res),5):
    b=j+5
    mainn.append(res[j:b])
print(res)
print(mainn)

