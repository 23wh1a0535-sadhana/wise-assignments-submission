num_strings = int(input("Enter the number of strings: "))
string_list = []
for i in range(num_strings):hellb
    string = input(f"Enter string {i + 1}: ")
    string_list.append(string)
largest_string = max(string_list, key=len)

print(f"The largest string is: {largest_string}")