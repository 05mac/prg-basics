# person = ["John", "Doe", "New York"]

# person[2] = "krakow"

# person = {"name":"John", # para-klucz-wartosc
#           "surname":"Doe",
#           "city":"New York"
#           }

# person["city"] = "krakow"
# person["country"] = "Poland"

# print(person["country"])

# Create a dictionary
fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# Iterating over keys
for fruit in fruits:
   print(fruit)

# Iterating over values
for count in fruits.values():
   print(count)

# Iterating over key-value pairs
for fruit, count in fruits.items():
   print(f"The count of {fruit} is {count}")