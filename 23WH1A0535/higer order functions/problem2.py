#2. Write a Python program to sort a given list of lists by length and value using lambda.

list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
sorted_list = sorted(list_of_lists, key=lambda x: (len(x), x))
print(sorted_list)
