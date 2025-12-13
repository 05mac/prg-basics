def f(value):
    # Nazwa pliku jest założeniem zadania
    file_name = 'data.csv'
    count = 0

    try:
        # Używamy encoding='utf-8', aby uniknąć problemów z polskimi znakami.
        with open(file_name, 'r', encoding='utf-8') as file:
            
            # Pomiń nagłówek, jeśli istnieje (np. "Imie,Nazwisko,Pensja")
            header = next(file) 
            
            for line in file:
                # 1. Podziel linię na części
                parts = line.strip().split(',') # .strip() usuwa białe znaki na końcu, w tym \n
                
                # Uważaj: zakładamy, że pensja jest na indeksie 3
                if len(parts) > 3: 
                    salary_str = parts[3]
                    
                    try:
                        # 2. Konwersja na liczbę (jeśli to float, użyj float())
                        salary_value = int(salary_str)
                        
                        # 3. Porównanie z podaną wartością
                        if salary_value >= value:
                            count += 1
                    except ValueError:
                        # Ochrona przed błędami, jeśli pensja nie jest liczbą
                        continue 
                        
        return count
    
    except FileNotFoundError:
        print(f"Błąd: Plik {file_name} nie został znaleziony.")
        return 0 # Zwracamy 0, jeśli plik nie istnieje

if __name__ == "__main__":
    Testy z kolokwium:
    (Założenie: funkcja f(value) zwraca liczbę)
    Musisz mieć plik data.csv w tym samym folderze!
    
    print(f(9200))   # Oczekiwany wynik: do porównania z innymi studentami
    print(f(11640))  # Oczekiwany wynik: do porównania z innymi studentami
    pass