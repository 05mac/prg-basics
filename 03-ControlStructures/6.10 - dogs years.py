# 1. Zmieniamy nazwę zmiennej wejściowej, aby pasowała do pytania ("human years")
human_years = int(input("Podaj wiek psa w ludzkich latach: "))

# 2. Najpierw sprawdzamy błędy (walidacja danych)
if human_years < 0:
    print("Wiek nie może być ujemny.")
else:
    # 3. Logika obliczeń
    if human_years <= 2:
        # Pierwsze 2 lata
        dog_years = human_years * 10.5
    else:
        # Powyżej 2 lat
        # Pierwsze 2 lata to zawsze 21, reszta razy 4
        dog_years = 21 + (human_years - 2) * 4

    # 4. Wypisanie wyniku tylko RAZ na samym końcu
    # Dzięki temu, jeśli zechcesz zmienić treść komunikatu, robisz to w jednym miejscu.
    print(f"Na pieskie lata to: {dog_years}")


# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

# jesli pies bedzie mial 10 lat to tylko 3 lata liczymy 
# jako 2 * 10.5 a ostatnie 7 jako 8 * 4 i sumujemu obie liczby
# popraw ------------------