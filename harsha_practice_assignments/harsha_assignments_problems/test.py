from itertools import permutations

largest = -1
list_com=[]
innum = input("Enter input number : ")
combinations_number =permutations(innum,len(innum))
for combination in combinations_number:
    # print(combination)
    num="".join((combination))
    # print(num)

    if num==num[::-1]:
        # print(num)
        # print(num)
        list_com.append(num)
        if largest<int(num):
            largest=int(num)


print('largest_num',largest)
print(set(list_com))