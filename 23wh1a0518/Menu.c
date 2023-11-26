def menu():
    dishes = ["1. rice","2. chicken","3. noodles"]
    for i in dishes:
      print(i)
def submenu():
    c=int(input("enter your choice: "))
    rice_dishes={"1. veg fried rice":180,"2. veg briyani":250,"3. veg pulao":300,"4. ghee rice":100,"5. curd rice":100}
    chicken = {"1. chicken briyani":400,"2.chicken mandi":500,"3. chicken 65":230,"4. chicken tandoori":230,"5. chicken lollipop":200}
    noodles = {"1. veg noodles":180,"2. mushroom noodles":200,"3. egg noodles":190,"4. chicken noodles":250,"5. garlic noodles":200}
    print(list(rice_dishes.keys()))
    print(list(chicken.keys()))
    print(list(noodles .keys()))
    if c==1:
        for x in rice_dishes:
         print(x)
    elif c==2:
        for x in chicken:
          print(x)
    elif c==3:
        for x in noodles:
          print(x)
    else:
        print("sorry! wrong choice")
    print(list(rice_dishes.values()))


submenu()
OUTPUT:

enter your choice: 2
['1. veg fried rice', '2. veg briyani', '3. veg pulao', '4. ghee rice', '5. curd rice']
['1. chicken briyani', '2.chicken mandi', '3. chicken 65', '4. chicken tandoori', '5. chicken lollipop']
['1. veg noodles', '2. mushroom noodles', '3. egg noodles', '4. chicken noodles', '5. garlic noodles']
1. chicken briyani
2.chicken mandi
3. chicken 65
4. chicken tandoori
5. chicken lollipop
[180, 250, 300, 100, 100]
