
print("------ Analizator cen ------")

cena_bez_promki = float(input("Podaj cene przedmiotu bez promocji: ")) 
cena_z_promka = float(input("Podaj cene przedmiotu już z promocją: "))

roznica_ceny = (cena_bez_promki - cena_z_promka) / cena_bez_promki

if roznica_ceny >= 0.1:
    print(f"Current product price: {cena_z_promka}")
    print(f"Previous product price: {cena_bez_promki}")
    print("Buy the product!!")
    print(f"Product price reduces by {roznica_ceny * 100:.0f}%")
else:
    print("Don't buy the product")
    



