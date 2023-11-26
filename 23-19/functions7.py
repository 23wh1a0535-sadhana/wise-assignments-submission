cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
string_of_cities = ""
for city in cities:
    string_of_cities += city + ", "
string_of_cities = string_of_cities[:-2] 
print(string_of_cities)
