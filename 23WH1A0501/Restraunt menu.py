#Restraunt
def mainmenu():
    dishes = ["1. Rice" , "2. Chicken" , "3. Noodles"]
    for i in dishes:
        print(i)

def submenu():
    mainmenu()
    choice1 = int(input("Enter your choice number: "))
    ricedishes = {"1. Veg Fried rice" :  180 , "2. Veg Biriyani" : 250 , "3. Veg Pulao" : 120, "4. Ghee rice" : 120, "5. Curd RIce" : 100}
    chicken_dishes = {"1. Chicken Biryani" : 330, "2. Chicken Mandi" : 450, "3. Chicken Lollipop" : 220, "4. Chicken 65" : 190, "5. Chicken manchurian" : 130, "6. Chicken Shewarma" : 190}
    noodle_dishes = {"1. Veg Noodles" : 80, "2. Mushroom noodles" : 100, "3. Egg noodles" : 90, "4. Chicken noodles" : 100, "5. Paneer noodles" : 100}
    ricekey = list(ricedishes.keys())
    ricevalues = list(ricedishes.values())
    chickenkey = list(chicken_dishes.keys())
    chickenvalues = list(chicken_dishes.values())
    noodlekey = list(noodle_dishes.keys())
    noodlevalues = list(noodle_dishes.values())
    if choice1 == 1:
        for i in ricekey:
            print(i)
        choice2 = int(input("Enter the dish number: "))
        a = choice2 - 1
        print(ricevalues[a])
    elif choice1 == 2:
        for i in chickenkey:
            print(i)
        choice2 = int(input("Enter the dish number: "))
        a = choice2 - 1
        print(chickenvalues[a])
    elif choice1 == 3:
        for i in noodlekey:
            print(i)
        choice2 = int(input("Enter the dish number: "))
        a = choice2 - 1
        print(noodlevalues[a])
    else:
        print("Sorry, Wrong choice entered")
submenu()