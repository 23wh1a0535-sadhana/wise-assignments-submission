#Write a program to print the largest string from a given list.
test_list = [ 'Cookies', 'Chocolate', 'Green', 'Apple']
lengths = [len(s) for s in test_list]
longest_index = lengths.index(max(lengths))
longest_string = test_list[longest_index]
print("Longest string is : " + longest_string)
