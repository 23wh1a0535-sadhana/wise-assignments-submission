def menu():
    dishes = ["1. Rice" , "2. Chicken" , "3. Noodles"]
    for i in dishes:
        print(i)

def price():
    menu()
    rice_dishes = {"1. Veg Fried Rice" : 95 , "2. Veg Biriyani" : 80 , "3. Veg Pulao" : 60 , "4. Ghee rice" : 70 , "5. jeera rice" : 40}
    chicken_dishes = {"1. Chicken biriyani" : 180 , "2. Chilly chicken" : 85 , "3. Chicken 65"  : 100 , "4. Chicken manchuriya " : 90 , "5. Chicken lollipop" : 120}
    noodles_dishes = {"1. Veg noodles" : 80 , "2. Egg noodles" : 90 , "3. Chicken noodles" : 100 , "4.mushroom noodles" : 100 , "5. Cup noodles" : 50}
    c = int(input("Enter your choice : "))
    if c == 1:
        for x in rice_dishes:
            print(x)
    elif c == 2:
        for x in chicken_dishes:
            print(x)
    elif c == 3:
        for x in noodles_dishes:
            print(x)
    else:
        print("Sorry a wrong choice")

    g= int(input("Enter your item : "))
    if g <= 5:
        print("Here you go ..!!")
    else:
        print("Check again .. sorry ")
    i = g-1
    if c <= 3:
        if c == 1:
            p = list(rice_dishes.values())[i]
            print(p)
        elif c == 2:
            q = list(chicken_dishes.values())[i]
            print(q)
        elif c == 3:
            r = list(noodles_dishes.values())[i]
            print(r)
    else:
        print("Please check your choice again...!!!")
