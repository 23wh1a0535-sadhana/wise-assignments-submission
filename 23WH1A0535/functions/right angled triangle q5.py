side1=int(input("Enter side 1 of triangle"))
side2=int(input("Enter side 2 of triangle"))
side3=int(input("Enter side 3 of triangle"))
if side1>side2 and side1>side3:
    if side1**2==side2**2 + side3**2:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")
elif side2>side1 and side2>side3:
    if side2**2==side1**2 + side3**2:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")
elif side3>side1 and side3>side2:
    if side3**2==side1**2 + side2**2:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")
