car_speed = int(input("Podaj prędkość: "))

speed_limit_min = 40
speed_limit_max = 140

if speed_limit_min<=  car_speed <= speed_limit_max:
    print(f"jedziesz {car_speed} na godzine i jest wszystko gites! ")
else:
    print(f"jedziesz {car_speed} na godzine co jest nieodpowiednie :/")
