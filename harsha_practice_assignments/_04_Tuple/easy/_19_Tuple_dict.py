lst = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

dic={}

for a,b in lst:
    dic.setdefault(a,[]).append(b)
    # print(a,b)
print(dic)