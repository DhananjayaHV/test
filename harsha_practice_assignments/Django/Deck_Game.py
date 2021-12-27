import random
player_name_1=input('Enter the name of player 1 : ')
player_name_2=input('Enter the name of player 2 : ')

def createDeck():
    spades = [10, 9, 8, 7, 6, 5, 4, 3, 2, "Js", "Qs", "Ks", "As"]
    clubs = [10, 9, 8, 7, 6, 5, 4, 3, 2, "Jc", "Qc", "Kc", "Ac"]
    diamonds = [10, 9, 8, 7, 6, 5, 4, 3, 2, "Jd", "Qd", "Kd", "Ad"]
    hearts = [10, 9, 8, 7, 6, 5, 4, 3, 2,"Jh", "Qh", "Kh", "Ah"]
    deck = spades + clubs + diamonds + hearts
    return deck

def random_suffl(lst):
    length=len(lst)
    for i in range(length):
        index = random.randint(i,length - 1)
        lst[i],lst[index] = lst[index],lst[i]
    return lst

def distribute(lst):
    p1=[]
    p2=[]
    count = 0
    for i in lst:
        if count%2==0:
            p1.append(i)
        else:
            p2.append(i)
        count+=1
    return p1,p2

def replace_in(chrt):
    for ch in chrt:
        if type(ch)==str:
            if 'A' in ch:
                chrt[chrt.index(ch)] = 14
            elif 'K' in ch:
                chrt[chrt.index(ch)] = 13
            elif 'Q' in ch:
                chrt[chrt.index(ch)] = 12
            elif 'J' in ch:
                chrt[chrt.index(ch)] = 11
    return chrt

def winner(p1,p2):
    if sum(p1)>sum(p2):
        print(f"Congratulations!!!\n{player_name_1} you are the Winner.")
        # print(f'{player_name_1} beat {player_name_2} by {sum(p1)-sum(p2)} points.')

    elif sum(p1)<sum(p2):
        print(f"Congratulations!!!\n{player_name_2} you are the Winner.")
        # print(f'{player_name_2} beat {player_name_1} by {sum(p2) - sum(p1)} points.')
    else:
        print(f'{player_name_1} and {player_name_2} got same score,hence match tied.')

def output():
    deck_list = createDeck()
    print("Deck Pack : ",deck_list)
    deck_shuffeled = random_suffl(deck_list)
    v1,v2=distribute(deck_shuffeled)
    print(f'cards of player {player_name_1} : ',v1)
    print(f'cards of player {player_name_2} : ',v2)
    player_p1=replace_in(v1)
    player_p2=replace_in(v2)
    print(f'Total value of the cards with {player_name_1} is :',sum(player_p1))
    print(f'Total value of the cards with {player_name_2} is :',sum(player_p2))
    winner(player_p1,player_p2)

output()
