def findlargestofthree(num1 , num2 , num3):
    if num1 > num2:
        if num1 > num3 :
            largest = num1
        else:
            largest = num3
    else:
        if num2 > num3:
            largest = num2
        else:
            largest = num3
    return largest
print(findlargestofthree(3 , 4 , 5))