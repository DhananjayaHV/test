
lst=[1,2,3,4,5,6,7,80]

for i in lst:
    for i in range(0,len(lst),2):
        lst[i],lst[i+1] = lst[i+1],lst[i]
print(lst)

# from itertools import zip_longest, chain, tee
# def replace2copy(lst):
#     lst1, lst2 = tee(iter(lst), 2)
#     return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
# n = [0,1,2,3,4,5]
# print(replace2copy(n))