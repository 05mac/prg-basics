 # 4. 
# person = {
#    "name": "Marek",
#    "surname": "Banach",
#    "age": 25,
#    "hobby": ["swimming","excursions"],
#    "married": True,
#    "phone":{"landline":"123444321","mobile":"777888999"}
# }

# print(person["name"])
# print(person["hobby"])
# print(person, end= "")
# person["surname"] = "Nowak"
# person["married"] = False
# person["gender"] = "male"
# person["hobby"].append("bicycle")
# person["phone"]["Work phone"] = "313131444"
# print(person)

# for k,v in person.items():
#     print(k,v)



# 5.
# countries = [
# {"name":"Poland", "population":38000000},
# {"name":"Germany", "population": 7000000},
# {"name":"Ukraine", "population": 555000},
# {"name":"USA", "population": 70064000},
# {"name":"Sweden", "population": 52355000}
# ]

# print(f"Country","Population")
# for elements in countries:
#     name = elements["name"]
#     population = elements["population"]

#     print(name,population)



# 6.
# phone_book = {
#    'John': '555-1234',
#    'David': '555-5678',
#    'Bob': '555-8765',
#    'Charlie': '555-4321',
#    'Diana': '555-9876',
#    'Eve': '555-6543',
#    'Frank': '555-3456',
#    'Grace': '555-7890',
#    'Hank': '555-1111',
#    'Ivy': '555-2222',
#    'Jack': '555-3333',
#    'Daniel': '555-4444',
#    'Liam': '555-5555',
#    'Mia': '555-6666',
#    'Nina': '555-7777',
#    'Oscar': '555-8888',
#    'Paul': '555-9999',
#    'Dominic': '555-1010',
#    'Rachel': '555-2020',
#    'Sam': '555-3030'
# }
# for element in phone_book:
#     if element[0] == "D":
#         print(phone_book[element])


# 7. 

# slownik = {
# 'Laptop': 15,
# 'Desktop PC': 10,
# 'Monitor': 25,
# 'Keyboard': 50,
# 'Mouse': 60,
# 'External Hard Drive': 30,
# 'Printer': 12,
# 'Router': 20,
# 'USB Flash Drive': 100,
# 'Graphics Card': 8
# }

# counter = 0
# for element,value in slownik.items():
#    print(f"{element}, - quantity {value}")
   
#    if value:
#     counter += value
# print(f"sum of products: {counter}")
#




# #8. 

# price_list = {
#    'T-shirt': 19.99,
#    'Jeans': 49.99,
#    'Jacket': 89.99,
#    'Sneakers': 59.99,
#    'Hat': 15.99
# }
# total_value_before_discount = 0
# total_value_after_discount = 0
# for product, price in price_list.items():
#     print(f"Product: {product} Price before the discount: {price} ")
#     total_value_before_discount += price

# print(f"total value of products before the discount: {total_value_before_discount:.2f}")


# print("------------Discount-------------")


# for product, price in price_list.items():
#     price *= 0.9
#     print(f"Product: {product} Price after the discount: {price:.2f} ")
#     total_value_after_discount += price


# print(f"total value of products after the discount: {total_value_after_discount:.2f}")


###### ############ SET ############ ######

# 2. 
# emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
# unique_emails = set(emails)  # Removes duplicates
# print(unique_emails)


# 3.

# all_students = {"Alice", "John", "Sara", "Bob"}
# attended_students = {"Alice", "Bob"}

# absent_students = all_students - attended_students  # Difference
# print(absent_students)

# 4.

# emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
# spam_list = {"spam1@example.com", "spam2@example.com"}

# spam_emails = spam_list  & emails_received   # Intersection
# print("Spam emails:", spam_emails)

# 5.

# contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
# contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# merged_contacts = contacts_A | contacts_B  # Union
# print("Merged contacts:", merged_contacts)
   

# 6. 

# required_permissions = {"read", "write", "execute"}
# user_permissions = {"read", "write"}

# has_permissions = required_permissions.issubset(user_permissions)  # subset
# print(has_permissions)  # Will return False because "execute" is missing


