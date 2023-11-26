#This program is to find the largest of three numbers.
def maximum(a, b, c): 
    if (a >= b) and (a >= c): 
        largest = a 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
    return largest 
print("Largest number is : ",maximum(5, 4, 9)) 
