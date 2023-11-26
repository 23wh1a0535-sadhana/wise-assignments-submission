def revnum(num):
    n = num
    revno = 0
    while n != 0:
        rem  = n % 10
        revno  = 10 * revno + rem
        n //= 10
    num = revno
    return num
number = int(input("Enter a number:"))
print(revnum(number))
