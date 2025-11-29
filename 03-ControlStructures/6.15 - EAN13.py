
numer_ean = int(input("Podaj 13 cyfrowy numer EAN-13: "))


if(len(str(numer_ean)) == 13):
    print("Numer produktu jest poprawny!")
    if str(numer_ean).startswith("590"):
        print("Produkt produkowany w Polsce")
    else:
        print("Produkt nie produkowany w Polsce")

else:
    print("Numer produktu sie nie zgadza, sprawdz poprawnosc")


