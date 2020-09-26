# Author: Elijah Khin
# Email:  workbiscap@gmail.com

# Description:
# Your task is to write a function maskify, which changes all but the last four characters into '#'.


def maskify(cc):
    if cc == '':
        return ''
    elif len(cc) < 4:
        return cc
    lst = []

    for x in range(len(cc[:-4])):
        k = '#'
        lst.append(k)
    for x in range(len(cc)-4, len(cc)):
        k = cc[x]
        lst.append(k)
    return ''.join(lst)


print(maskify('123'))


def maskify_not_mine(cc):
    return "#"*(len(cc)-4) + cc[-4:]

print(maskify_not_mine('123'))

















