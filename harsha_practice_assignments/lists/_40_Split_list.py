'''Split a list based on first character of word'''

word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

from itertools import groupby
from operator import itemgetter

class A:


    def __init__(self,lst):
        self.lst=lst


    def split_word(self):
        word_list=self.lst
        for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)




word_list1 = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']


a=A(word_list)
a.split_word()
# res=[letter,[wor for wor in words] for letter,words in groupby(sorted(word_list),key=itemgetter(0))]
print(">>>",a)

e=[x for x in [1,2,3]]
print(e)
    # print(">>",letter)
    # for i in words:
    #     print(i)
    # print(words)
    # for word in words:
    #     print(word)


#
# a=A(word_list)
# a.split_word()
