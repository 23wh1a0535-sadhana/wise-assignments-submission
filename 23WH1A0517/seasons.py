month=input("enter month:")
day=int(input("enter day:"))
if month=="march" or month=="february":
    print("spring")
elif month=="december" or month=="january":
    print("winter")
elif month=="april" or month=="may" or month=="june":
    print("summer")
elif month=="july" or month=="august":
    print("monsoon")
elif month=="september" or month=="october":
    print("fall")
elif month=="november":
    print("winter")
else:
    print("wrong data entered")