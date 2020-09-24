def is_square(n=0):
    return n > 0 and n**(1/2) - int(n**(1/2)) == 0


print(is_square(-9))


