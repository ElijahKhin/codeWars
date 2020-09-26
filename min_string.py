# Author: Elijah Khin
# Email:  workbiscap@gmail.com

# Description:
# My task is to return a min word in input string.



def find_short(s):

    word_length = 0
    all_words = []
    for i in range(len(s)):
        if s[i] != " ":
            word_length += 1
        else:
            all_words.append(word_length)
            word_length = 0
    else:
        all_words.append(word_length)
    for i in range(len(all_words)):
        for j in range(len(all_words)):
            if all_words[i] > all_words[j]:
                break
        else:
            return all_words[i]


def find_short1(s):
    return len(min(s.split(' '), key=len))


def find_short2(s):
    return min(len(x) for x in s.split())