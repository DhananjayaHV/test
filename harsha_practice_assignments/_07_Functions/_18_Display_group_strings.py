from itertools import groupby

my_list = ["I love cat","I love dog","I love fish","I hate banana","I hate apple","I hate orange"];

each_word = sorted([x.split() for x in my_list])

# I assumed the keywords would be everything except the last word
grouped = [list(value) for key, value in groupby(each_word, lambda x: x[:-1])]

result = []
for group in grouped:
    temp = []
    for i in range(len(group)):
        temp.append(" ".join(group[i]))
    result.append(temp)

print(result)