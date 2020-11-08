# Author: Elijah Khin
# Email:  workbiscap@gmail.com

# Description:
# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).


def solution(string, ending):
    return True if string[-len(ending):] == ending or len(ending) == 0 else False



