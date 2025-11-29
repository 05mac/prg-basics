# convert time 

czas_str = (input("Wprowadź 24-godzinny format godziny (GG:MM):  "))
godzina_str, minuta_str = czas_str.split(":")
godzina = int(godzina_str)


if godzina > 12 and godzina < 24 :
    godzina = godzina - 12
    print(f"jest godzina: {godzina}:{minuta_str}pm")
elif godzina == 12:
    print(f"jest godzina: {godzina}:{minuta_str}pm")
elif godzina == 00:
    godzina = godzina + 12
    print(f"jest godzina: {godzina}:{minuta_str}am")

else:
    print(f"jest godzina: {godzina}:{minuta_str}am")
