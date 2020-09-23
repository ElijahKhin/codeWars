# Elijah Khin
# workbiscap@gmail.com

# Description:
# In this Kata, I will be given a number and my task will be to return the nearest prime number.


import time


start_time = time.time()


def solve(n):

    lst = []
    add = 1
    do = True
    if n == 1:  # exception 1
        return 2
    elif n == 2:  # exception 2
        return 3

    for pls in range(n - 1, 1, -1):  # 'pls' - prime in left side
        for divider in range(2, (round(pls / 2) + 1)):
            if pls % divider == 0:
                break
        else:
            lst.append(pls)
            break

    while do is True:
        add += 1
        for divider in range(2, round((n+add) / 2) + 1):
            if (n + add) % divider == 0:
                break
        else:
            lst.append(n+add)
            break

    if n - lst[0] > lst[1] - n:
        return lst[1]
    else:
        return lst[0]


print(solve(8000000))


print(time.time() - start_time, 'new_alg')


