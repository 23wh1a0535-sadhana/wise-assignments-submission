telangana_cities = ["Hyderabad", "Warangal", "Karimnagar", "Nizamabad", "Khammam", "Ramagundam", "Mahbubnagar"]

user_city = input("Enter a city name: ")

result = f"{user_city} is in Telangana." if user_city.capitalize() in telangana_cities else f"{user_city} is not in Telangana."

print(result)