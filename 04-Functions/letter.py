def letter_appear (tekst,litera):
    licznik = 0
    for i in tekst:
        if i == litera:
            licznik += 1
    return licznik
           
if __name__ == "__main__":
    tekst = "You never get a second chance to make a first impression"
    print(letter_appear(tekst,"e"))
