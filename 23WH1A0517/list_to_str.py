# Python program to convert a list to string

def listToString(s):

	# initialize an empty string
	str1 = ""

	# traverse in the string
	for ele in s:
		str1 += ele

	# return string
	return str1
# Driver code
s = ['sarah', 'sameera', 'peruka']
print(listToString(s))

