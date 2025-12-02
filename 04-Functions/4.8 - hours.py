def time_string(hours, minutes, time_format):
    
    # Sprawdzamy, czy dane są poprawne, w tym 0 <= minutes <= 59 (poprawione w Twoim kodzie)
    if 0 <= hours <= 23 and time_format == '24' and 0 <= minutes <= 59:
        
        # *** POPRAWKA: Użycie f-strings dla zer wiodących ***
        # :02d oznacza formatowanie liczby całkowitej (d) na 2 miejsca z zerem wiodącym (02)
        minutes_str = f"{minutes:02d}"
        hours_str = f"{hours:02d}"
        
        # Zwracamy poprawnie sformatowane napisy (np. "08:03")
        return hours_str + ":" + minutes_str

    elif 0 <= hours <= 23 and time_format == '12' and 0 <= minutes <= 59:
        
        # --- Definicja minut sformatowanych (wymagana we wszystkich 12h przypadkach) ---
        minutes_str = f"{minutes:02d}"
        
        # --- Północ (00:xx) -> 12:xx am ---
        if hours == 0:
            hours += 12 # 0 zamieniamy na 12
            return str(hours) + ":" + minutes_str + "am"

        # --- Przedpołudnie (1:xx do 11:xx) ---
        elif hours < 12:
            # Nie zmieniamy godzin, tylko formatujemy minuty
            return str(hours) + ":" + minutes_str + "am"
            
        # --- Południe (12:xx) -> 12:xx pm ---
        elif hours == 12:
            # Nie zmieniamy godzin
            return str(hours) + ":" + minutes_str + "pm"
            
        # --- Popołudnie/Wieczór (13:xx do 23:xx) ---
        elif hours > 12:
            hours -= 12 # Odejmujemy 12 (np. 15 -> 3, 19 -> 7)
            return str(hours) + ":" + minutes_str + "pm"

# Dodatkowa obsługa nieprawidłowego formatu czasu
    return "Invalid Time Format or Input"


print(time_string(15, 38, '24'))   # 15:38
print(time_string(8, 3, '24'))     # 08:03
print(time_string(0, 5, '24'))     # 00:05
print(time_string(11, 15, '12'))   # 11:15am
print(time_string(0, 7, '12'))     # 12:07am
print(time_string(7, 30, '12'))    # 7:30am
print(time_string(12, 46, '12'))   # 12:46pm
print(time_string(13, 10, '12'))   # 1:10pm
print(time_string(19, 0, '12'))    # 7:00pm