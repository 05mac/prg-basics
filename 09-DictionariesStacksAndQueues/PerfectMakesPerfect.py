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


# ---------------------- PRATICE MAKES PERFECT ----------------#


# # 14.
# import queue
# kolejka_biuro = queue.Queue()

# nastepny_numer_biletu = 1

# while True:
#     print("Witamy!. System obłsugi klienta")
#     print("1. Pobierz bilet (Nowy Klient)")
#     print("2. Obsłuż klienta")
#     print("0. Zamknij system")

#     opcja = (input("Wybierz opcje: "))

#     if opcja == "1":
#         bilet = nastepny_numer_biletu
#         kolejka_biuro.put(bilet)
#         print(f"Zostałeś dodany do kolejki, twój numer to: {bilet}")
#         nastepny_numer_biletu += 1


#     elif opcja == "2":
#         if not kolejka_biuro.empty():
#             numer_do_obslugi = kolejka_biuro.get()
#             print(f"numer: {numer_do_obslugi} w trakcie oblugi!")
#         else:
#             print(f"Brak klientow do obsługi!")
#     elif opcja == "0":
#         print("Zamykanie systemu...")
#         break



#3. 

# translations = {
#    'computer': 'komputer',
#    'mouse': 'myszka',
#    'keyboard': 'klawiatura',
#    'printer': 'drukarka'
# }

# word = input("Enter a word to translate(computer stuff): ")

# if word in translations:
#     print(translations[word])
# else:
#     print(f"translation of '{word}' is unavailable")


# 4. 

# winter_semester = {
#    "math":60,
#    "programming":30,
#    "history":15
# }
# hours = 0
# for i in winter_semester.values():
#     hours += i
# print(hours)




# 5.
# paragraph = "cat dog mouse cat rat cat mouse"
# paragraph = paragraph.split()

# print(len(paragraph))



#6. 

# basic_data = {
#    "name":"Barbara",
#    "age":21
# }

# advanced_data = {
#    "status":"student",
#    "married":False,
#    "interest":["reading","swimming"]
# }

# person = {}
# person.update(basic_data)
# person.update(advanced_data)

# print(person)


# 7. 

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
def hotel_list(hotels):
    dictOFhotels = {}
    if hotels == "Krakow":
        for i in hotels_in_Krakow:
            for i in
def avg_price(hotels):
    pass

print(hotel_list('Krakow'))