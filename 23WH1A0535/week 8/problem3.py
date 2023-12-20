#Problem 3
#Start with any number. (For practice try small numbers) say 7if it is even divide by 2, if it is odd multiply by 3 and add 1
#Repeat THis process reaches at ...4, 2, 1 and then starts repeating
#Write a function that generates the sequence ending in 4, 2, 1 for the given starting number
#For example 7 should generate [7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]


def generateCollatz(num:int):
    while True:
        print(num)
        if num == 1:
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1


generateCollatz(7)

#General format
generateCollatz(int(input("Enter the number for which the collatz sequence is to be generated: ")))
