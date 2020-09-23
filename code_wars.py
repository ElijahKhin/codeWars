import time


start_time = time.time()


def solve(n):
    if n == 1:  # exception 1
        return 2
    elif n == 2:  # exception 2
        return 3

    score = 0
    number_is_found = False

    for pls in range(n - 1, 1, -1):  # 'pls' - prime in left side
        for divider in range(2, round(pls / 2) + 1):
            if pls % divider != 0:
                score += 1
            else:
                break
            if score == len(range(2, round(pls / 2) + 1)):
                # print(f'{pls} <------- this number is the nearest prime! (left side)')
                number_is_found = True
        if number_is_found:
            break

    score = 0
    number_is_found = False
    prs = n  # 'prs' - prime in right side
    while number_is_found is not True:
        prs += 1
        for divider in range(2, round(prs / 2) + 1):
            if prs % divider != 0:
                score += 1
            else:
                break
            if score == len(range(2, round(prs / 2) + 1)):
                # print(f'{prs} <------- this number is the nearest prime! (right side)')
                number_is_found = True

    if prs - n > n - pls:
        return pls
    elif prs - n == n - pls:
        return pls
    else:
        return prs


print(solve(500))

print(time.time() - start_time, 'second_exp')
