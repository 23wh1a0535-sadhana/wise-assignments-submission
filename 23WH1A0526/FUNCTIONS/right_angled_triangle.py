#For checking the triangle is right angled triangle or not.
def right_angled(a, b, c):
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        return "The triangle is right-angled." 
    else:
        return "The triangle is not right-angled."
right_angled(3,4,5)
