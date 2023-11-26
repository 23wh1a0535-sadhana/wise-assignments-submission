month=input("enter month name:")
if month=="January" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
    print("31 days")
elif month=="february":
    print("29 days")
else:
    print("30 days")