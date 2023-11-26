def int_to_list_method_3(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number //= 10
    return digits
number = int(input("enter num:"))
result = int_to_list_method_3(number)
print(result)