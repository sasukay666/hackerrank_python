# HACKERRANK MINION GAME
# https://www.hackerrank.com/challenges/the-minion-game/problem
#
# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
# STUART    KEVIN
# B-1       A-3
# N-2       AN-2
# BA-1      ANA-2
# NA-2      ANAN-1
# BAN-1     ANANA-1
# NAN-1
# BANA-1
# NANA-1
# BANAN-1
# BANANA-1
# output - Stuart 12


def minion_game(string):
    string = string.split()
    string = ''.join(string)
    vowels = 'aeiouAEIOU'
    list = []
    stre = ''
    k, s = 0, 0
    for e in string:
        if e not in stre:
            stre += e
    for e in stre:
        indx = string.index(e)
        for i in range(indx, len(string)):
            for j in range(i+1, len(string)+1):
                if string[i:j] not in list:
                    list.append(string[i:j])
    list.sort()

    for e in list:
        for i in range(len(string)):
            if string[i:len(e)+i] == e:
                if e[0] not in vowels:
                    s += 1
                elif e[0] in vowels:
                    k += 1
    if s>k:
        print('Stuart '+str(s))
    elif s<k:
        print('Kevin '+str(k))
    elif s==k:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

# # Alternate Solution from HackerRank community
# s = input()
# vowels = 'AEIOU'
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")

