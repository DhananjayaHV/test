from itertools import combinations
msg='BANANA'.lower()
ovwel=['a','e','i','o','u']
# for j  in range(len(msg)+1):
    # a=combinations(msg,j)
str2=[]
lst=[]
sub_strng=[]
playerA={}
playerB={}
for i in range(1,len(msg)+1):
    lst.append(list(combinations(msg, i)))
    # print(lst)
for i in lst:
    for item in i:
        sub_str=''.join(item)
        sub_strng.append(sub_str)
# print(sub_strng)

for i in sub_strng:
    # print(i[0])

    if i[0] in ovwel:
        playerA[i]=playerA.get(i,0)+1
    else:
        playerB[i]=playerB.get(i,0)+1

if len(playerA.values())>len(playerB.values()):
    print("playerA is winner.")
else:
    print("PlayerB is winner.")
print(playerA)
print(playerB)


'''
import itertools


class A:

    def __init__(self):
        self.msg=input("Enter the input string : ").lower()

    def words_combination_generator(self):
        lst=[]
        words=[]
        for i in range(1,len(self.msg)+1):
            lst.append(list(itertools.combinations(self.msg, i)))
        print(lst)

        for element in lst:
            for j in element:
                words.append(''.join(j))
        print("All possible combinations of words are :",words)
        return words


    def sub_string_generator(self,list_words):
        ovwels=['a','e','i','o','u']
        player_ovwel={}
        player_consonants={}

        for word in list_words:
            if word[0] in ovwels:
                player_ovwel[word]=player_ovwel.get(word,0)+1
            else:
                player_consonants[word]=player_consonants.get(word,0)+1

        return player_ovwel,player_consonants




    def winner_declarator(self,dic1,dic2):
        if len(dic1.values())>len(dic2.values()):
            print("Player A is winner.")
        else:
            print("Player B is winner.")



a=A()
b=a.words_combination_generator()
x,y=a.sub_string_generator(b)
print('x',x)
print("y",y)
a.winner_declarator(x,y)




'''
