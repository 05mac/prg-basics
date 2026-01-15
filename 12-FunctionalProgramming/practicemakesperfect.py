#///////////////////// Practice Makes Perfect //////////

#4. 

# array = list(range(1,21))

# potega_trzy = list(map(lambda x: x**3 , array))
# print(potega_trzy)


#///////////////////// Practice Makes Perfect //////////


# #5. 

# array = list(range(1,21))

# numbers = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, array))
# print(numbers)


#///////////////////// Practice Makes Perfect //////////

# 6. 

# array = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
#    ("Jackson","Peter"),("Johnson","Rick"),
#    ("Lewis","Terry"),("Clarke","Robin")]

# nazwiska = list(map(lambda x: f"{x[0]}, {x[1]}",array))

# lista_nazwisk = "\n".join(nazwiska)
# print(lista_nazwisk)


#///////////////////// Practice Makes Perfect //////////

# 7. 

# ratings = [(17,15,16,17,15),
#  (16,18,19,17,19),
#  (19,15,15,19,18),
#  (18,17,19,15,16)]

# suma_ocen = list(map(lambda x: sum(x) - max(x) - min(x),ratings ))
# print(suma_ocen)

#///////////////////// Practice Makes Perfect //////////

# # 8.

# grades = [37,51,44,23,78,92,39,84,83,51]

# def min_pts(limit):
#    return lambda pts: pts>=limit


# oceny = list(filter(min_pts(70),grades))
# oceny2 = list(filter(min_pts(40),grades))
# oceny3 = list(filter(min_pts(30),grades))
# print(f"Min 70 pts: {oceny}")
# print(f"Min 40 pts: {oceny2}")
# print(f"Min 30 pts: {oceny3}")



#///////////////////// Practice Makes Perfect //////////

# # 9.

# temperatury = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

# plusy = list(filter(lambda x: x[1] > 0 , temperatury.items()))
# miasta = list(map(lambda x: x[0] ,plusy))

# napis = ' '.join(miasta)
# print(f"Cities with positive temperatures: {napis}")



#///////////////////// Practice Makes Perfect //////////

# # # 10.

# temperatury = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}






#///////////////////// Practice Makes Perfect //////////

# # # 11.

# test_results = [
#    {"name":"Peter","result":27},
#    {"name":"Anna","result":63},
#    {"name":"Robert","result":92},
#    {"name":"Paul","result":46},
#    {"name":"Barbara","result":52}]

# score = list(filter(lambda x: x["result"] in range(50,71), test_results))
# print(score)


#///////////////////// Practice Makes Perfect //////////

# # # # 12. 

# countries = [
#     {"country":"Denmark","gold":2,"silver":4,"bronze":6},
#     {"country":"Finland","gold":5,"silver":0,"bronze":4},
#     {"country":"USA","gold":12,"silver":5,"bronze":11},
#     {"country":"Peru","gold":0,"silver":1,"bronze":7}
# ]

# medals = list(filter(lambda x: x["gold"] + x["silver"] + x["bronze"] >= 10 ,countries ))
# print(medals)
# numbers = list(map(lambda x: F"{x["country"]}: {x["gold"]}, {x["silver"]}, {x["bronze"]}", medals))
# print("\n".join(numbers))


#///////////////////// Practice Makes Perfect //////////

# # # # 14. 

bottles = [508,500,512,499,492,511,503,476,501,509]


niepoprawne = list(filter(lambda x: x not in range (490, 511),bottles))
wynik = (len(niepoprawne) / len(bottles)) * 100
print(F"{wynik:.0f}%")