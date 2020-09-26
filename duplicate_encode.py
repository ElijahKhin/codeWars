# Author: Elijah Khin
# Email:  workbiscap@gmail.com

# Description:
# The goal of this exercise is to convert a string to a new string
# where each character in the new string is "("
# if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word):
    lst = []
    work_word = word.lower()
    for x in range(len(word)):
        if work_word.count(work_word[x], 0) > 1:
            lst.append(')')
        else:
            lst.append('(')

    return ''.join(lst)


# This code below isn't mine. I just like it.
def duplicate_encode1(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


print(duplicate_encode(word='(mn8M)(6kKH'))
print(duplicate_encode1(word='(mn8M)(6kKH'))


