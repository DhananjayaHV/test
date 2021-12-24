tup1=(1,2,3,4,5,6)
tup_dic={}
for i in tup1:
    tup_dic[i]=tup_dic.get(i,0)+1
print(tup_dic)


def Convert(tup):
    di={}
    di = dict(tup)
    return di



def cnv(tup):
    di=dict(tup)
    print(di)

tp=((1,2),(3,4))
cnv(tp)

# Driver Code
tups = ((12,13),)
print(Convert(tups))