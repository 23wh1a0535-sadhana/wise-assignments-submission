def ifrightangled(x1 , y1 , x2 , y2 , x3 , y3):
    ABsquared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    BCsquared = (x1 - x3) ** 2 + (y1 - y3) ** 2
    CAsquared = (x2 - x3) ** 2 + (y2 - y3) ** 2
    count = 0
    if ABsquared > BCsquared:
        if ABsquared > CAsquared:
            if ABsquared == BCsquared + CAsquared:
                count = 1
        else:
            if CAsquared == ABsquared + BCsquared:
                count = 1
    else:
        if BCsquared > CAsquared:
            if BCsquared == ABsquared + CAsquared :
                count = 1
        else:
            if CAsquared == ABsquared + BCsquared:
                count = 1
    if count == 0:
        return "Not a right triangle"
    else:
        return "right triangle"
print(ifrightangled(0 , 0 , 0 , 3 , 4 , 0))

