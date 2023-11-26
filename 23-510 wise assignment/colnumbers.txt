no_of_col = int(input("Enter the number of columns required(only odd number): "))
for i in range((no_of_col+3)//2):
    print("*"*i)
for i in range(1 , (no_of_col+1)//2):
    print("*"*(((no_of_col+1)//2) - i))