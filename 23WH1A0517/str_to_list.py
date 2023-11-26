# Python code to convert string to list


def Convert(string):
	li = list(string.split(" "))
	return li


# Driver code
str1 = "sarah sameera "
print(Convert(str1))
