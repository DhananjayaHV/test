L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]

# Approch 1:
# ==========
res=[]
for i in L:
    # print(i)
    for j in i:
        res.append(j)
print(sorted(set(res)))

# Approch 2:
# ===========
print("Sorted union list : ",sorted(set().union(*L)))


'''doubt on this'''

# Approch 3:
# ============
final=[j for j in i for i in L]

print(final)