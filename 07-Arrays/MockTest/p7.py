import re
def f (array):
# nie moze byc "." 

# tylko znaki od 4 - 12
# male litery
#liczby
#podkreslenia
    tablica_poprawnych_znakow = ['_']
    licznik = 0
    n = len(array)
    pattern = re.compile(r"^[a-z0-9_]{4,12}$")
    for i in array:
        if pattern.match(i):
            licznik += 1

    return licznik
        

if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
 