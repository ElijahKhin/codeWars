def is_square(n=0):
    if n < 0:
        return False
    if n**(1/2) - int(n**(1/2)) == 0:
        return True
    else:
        return False


