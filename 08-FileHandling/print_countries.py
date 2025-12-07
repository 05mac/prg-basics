###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    licznik = 1
    for line in file:
        print(f"{licznik}.{line}", end="")
        licznik += 1