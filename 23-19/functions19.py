num = int(input("Enter a number:"))
def sqrt(num):
    count=0
    for i in range(1,num):
        if num==i*i:
            print(i)
            count+=1
    if count==0:
        print("check your number")
sqrt(num)
