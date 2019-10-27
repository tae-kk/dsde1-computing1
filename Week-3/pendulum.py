def period(L, g):
    import math
    T = 2 * math.pi*math.sqrt(L/g)
    if g == 0:
        raise ZeroDivisionError("g cannot be zero")
    if isinstance(L, str) == True:
        raise TypeError ("L is a number")
    if L < 0:
        raise ValueError ("L is a positive value")
    if isinstance(g, str) == True:
        raise TypeError ("g is a number") 
    if g < 0:
        raise ValueError ("g is greater than 0")
    else:
        return T





