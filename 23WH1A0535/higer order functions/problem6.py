#6. Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
result_dict = dict(zip(lst1, lst2))
print(result_dict)
