def swap(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    return a,b 
a=int(input("enter num1:"))
b=int(input("enter num2:"))
swap(a,b)
print(swap(a,b))