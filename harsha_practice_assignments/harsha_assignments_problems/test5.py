'''
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids
For Mary George, the output should be:

Ms. Mary George
Input Format

The first line contains the integer , the number of people.
 lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints


Output Format

Output  names on separate lines in the format described above in ascending order of age.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''



# # collect=[['dhanu', 'hv', '20', 'm'], ['ganesh', 'kadali', '22', 'f'], ['sohel', 'fazal', '12', 'm'], ['kundan', 'kumar', '17', 'm']]
# for i in range(4):
#     name=input('Enter :').split(' ')
#     collect.append(list(name))
# new_list=sorted(collect,key=lambda x:x[2])
# for person in new_list:
#     print(("Mr. " if person[3] == "m" else "Ms. ") + person[0] + " " + person[1])
#


'''
dhanu hv 20 m
ganesh kadali 22 f
sohel fazal 12 m
kundan kumar 17 m
'''

import operator

def person_lister(f):
    def inner(people):
        new_list=sorted(people,key=lambda x:x[2])
        for i in new_list:
            print(f(i))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "m" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))],
people=[['dhanu', 'hv', '20', 'm'], ['ganesh', 'kadali', '22', 'f'], ['sohel', 'fazal', '12', 'm'], ['kundan', 'kumar', '17', 'm']]
name_format(people)
# print(name_format(people), sep='\n')


def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

print("End")