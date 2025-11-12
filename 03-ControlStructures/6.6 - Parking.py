
numberOfHours = int(input("Ile godzin będziesz u nas parkował?: "))
if numberOfHours in (1,2):
    cenaPostoju = 5
elif numberOfHours in (3,6):
    cenaPostoju = 15
elif numberOfHours > 6:
    cenaPostoju = 20


print(f"Za {numberOfHours} godziny postoju zapłacisz {cenaPostoju}zł")
