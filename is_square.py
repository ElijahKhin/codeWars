# Elijah Khin
# workbiscap@gmail.com

# Description:
# I will be given a number and then I'll must answer a question: Is it square number?


def is_square(n=0):
    return n > 0 and n**(1/2) - int(n**(1/2)) == 0


print(is_square(-9))


