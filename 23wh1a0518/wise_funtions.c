#reverse a string
def rev_string(s):
    str= " "
    for i in s:
        str = i + str
    return str
s="Diya"
print(rev_string(s))


ayiD



#convert a number into a list of its digits.
user_no=int(input("enter a no"))
dig_list=[int(digit)for digit in str(user_no)]
print(dig_list)


enter a no6
[6]



#check if a given tringle is a right angled triangle or not.
def right_angled(a,b,c):
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        return"the triangle is right-angled."
right_angled(90,90,0)


'the triangle is right-angled.'  



#program to convert a string into a list.
s="Diya Mandal"
x=list(s)
print(x)


['D', 'i', 'y', 'a', ' ', 'M', 'a', 'n', 'd', 'a', 'l']




#program to convert a list into string.
list=["apple","banana","cherry"]
res_string=",".join(list)
print(res_string)


apple,banana,cherry




#check whether the entered city name is present in telangana state or not.
telangana_cities=["Hyderabad","Warangal","Karimnagar","Nizamabad","Khammam","Ramagundam","Mahabubnagar"]
user_city=input("enter a city name:")
result=f"{user_city} is in Telangana."if user_city.capitalize() in telangana_cities else f"{user_city} is not in Telangana."
print(result)


enter a city name:Hyderabad
Hyderabad is in Telangana.




#calculate length of a string entered by user.
str=input("enter a string:")
#using len() funtion to find length of str
print("length of the input string is:",len(str))


enter a string:diya060605
length of the input string is: 10




#a program to reverse a given digit
num=int(input("enter number:"))
revs_number=0
while (num>0):
    reminder = num % 10
    reversed_num = (revs_number*10) + reminder
    num=num//10
print("reverse is :",revs_number)


enter number:060605
reverse is : 0




#print the largest string from a given list.input should be given by the user.
test_list=['cookies','chocolate','green','apple']
lengths=[len(s) for s in test_list]
longest_index=lengths.index(max(lengths))
longest_string=test_list[longest_index]
print("longest string is:"+longest_string)


longest string is:chocolate




#progrm to add up numbers in a given list.
numlist=[2,4,2,5,7,9,23,4,5]
numsum=sum(numlist)
print('sum of list:',numsum)
#example with start
numsum=sum(numlist,5)
print('sum of list:',numsum)


sum of list: 61
sum of list: 66




#program to sort an array
arr=[5,9,1,10,3,8,4,2,7,6]
temp=0
max_size=len(arr)
print("the elements of the arry before sorting:");
for i in range(0,max_size):
    print(arr[i],end=" ")
print()
for i in range(0,max_size):
    for j in range(i+1, len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("the element of the arry after sorting:")
for i in range(0,max_size):
    print(arr[i],end=" ")


the elements of the arry before sorting:
5 9 1 10 3 8 4 2 7 6 
the element of the arry after sorting:
1 2 3 4 5 6 7 8 9 10 




#program to find the LCM of two numbers.
def compute_LCM(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            LCM = greater
            break
        greater += 1
    return LCM
num1 = 23
num2 = 21
print("the L.C.M. is", compute_LCM(num1,num2))


the L.C.M. is 483




#palindrom or not
def ispalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] !=str[len(str)-i-1]:
            return False
        return True
s="mom"
ans=ispalindrome(s)
if (ans):
    print("Yes")
else:
    print("No")


Yes




#gretest number among given three number
num1=12
num2=6
num3=33
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("the largest number is",largest)


the largest number is 33




#program to swap to number
x = 5
y = 10
temp = x
x = y
y = temp
print('the value of x after swapping:{}'.format(x))
print('the value of y after swapping:{}'.format(y))


the value of x after swapping:10
the value of y after swapping:5




#program to convert a decimal number to a binary number
def decimaltobinary(num):
    if num >= 1:
        decimaltobinary(num // 2) 
    print(num % 2, end = '')
if __name__ == '__main__':
    dec_val = 24
    decimaltobinary(dec_val)


011000




#program to find the squre root of a number.
n = 4

square = n ** 2

print(square)


16




#program to count occurrence of character in string
input_string = "Diya"
print("the input string is:", input_string)
myset = set(input_string)
for element in myset:
    countofchar = 0
    for character in input_string:
        if character == element:
            countofchar += 1
    print("count of character '{}' is {}".format(element, countofchar))


the input string is: Diya
count of character 'a' is 1
count of character 'D' is 1
count of character 'y' is 1
count of character 'i' is 1




#program to remove vowels from the string
string = "hello"
vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
    print("\nAfter removing Vowels:",result)


After removing Vowels: h

After removing Vowels: h

After removing Vowels: hl

After removing Vowels: hll

After removing Vowels: hll


