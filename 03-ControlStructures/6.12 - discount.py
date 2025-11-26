# (2 * 40) + (3 * 30)

liczba_przedmiotow = int(input("Podaj liczbę zakupionych prodkutów: "))
cena_przedmiotu = float(input("Podaj cenę za sztukę: "))

if liczba_przedmiotow < 0:
    print("liczba przedmiotow nie moze byc ujemna")
else:
    if liczba_przedmiotow < 2:
        print("Nie ma dla ciebie zadnej promocji")
        print(f"kwota do zaplaty: {liczba_przedmiotow * cena_przedmiotu}")
    else:
        print(f"kwota do zaplaty: {2 * cena_przedmiotu + (cena_przedmiotu - cena_przedmiotu * 0.75 ) * (liczba_przedmiotow - 2)}")

