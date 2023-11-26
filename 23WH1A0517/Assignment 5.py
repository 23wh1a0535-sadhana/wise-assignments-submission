string=input("enter a string")
letters=sum(c.isalpha() for c in string)
dig=sum(c.isdigit() for c in string)
print(f"letters : {letters},digits:{dig}")
