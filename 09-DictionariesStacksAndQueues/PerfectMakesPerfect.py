person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])
print(person, end= "")
person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobby"] = "basketball"


