punkt = (input("Podaj współrzędne punktu w formacie x,y "))
x_str, y_str = punkt.split(",")
x = int(x_str)
y = int(y_str)


# 1 przypadek - x > 0 i y > 0 - cwiartka 1
# 2 przypadek - x < 0 i y > 0 - cwiartka 2
# 3 przypadek - x < 0 i y < 0 - cwiartka 3
# 4 przypadek - x > 0 i y < 0 - cwiartka 4 
# 5 przypadek - x == 0 lub y == 0 - brak cwiartki

if x == 0 and y == 0:
    print(f"Point P({punkt}) is at the origin of the coordinate system (0,0)")
elif x == 0:
    print(f"Point P({punkt}) is on the Y axis")
elif y == 0:
    print(f"Point P({punkt}) is on the X axis")
elif x > 0 and y > 0:
    print(f"Point P({punkt}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({punkt}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({punkt}) is in the third quadrant of the coordinate system")
else:
    print(f"Point P({punkt}) is in the fourth quadrant of the coordinate system")