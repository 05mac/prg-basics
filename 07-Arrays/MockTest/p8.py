def f(expression):
    stos = []
    
    # 1. Poprawny podział na tokeny (lista stringów: ['11', '7', '+', '15', '-', '14', '+'])
    tokens = expression.split() 
    
    for token in tokens: # Zmieniamy zmienną iteracyjną na 'token'
        
        # 2. Sprawdzanie, czy token to liczba (obsługa wielocyfrowych)
        if token.isdigit():
            # Dodajemy CAŁY TOKEN (np. '11') po konwersji na liczbę (11)
            stos.append(int(token)) 
            
        # 3. Jeśli to operator, wykonaj operację
        elif token == "+": # Używamy 'elif' dla lepszej logiki
            ostatnia = stos.pop() 
            przedostatnia = stos.pop() 
            wynik = przedostatnia + ostatnia # Operujemy już na liczbach!
            stos.append(wynik)
            
        elif token == "-":
            ostatnia = stos.pop()
            przedostatnia = stos.pop()
            wynik = przedostatnia - ostatnia # Prawidłowa kolejność RPN
            stos.append(wynik)
        
        # Opcjonalnie: dodaj operatory * i /

    # 4. Na koniec zwracamy wynik
    if stos: # Sprawdzenie, czy stos nie jest pusty
        return stos[0]
    return None # Zwracamy None, jeśli wyrażenie jest nieprawidłowe

print(f("11 7 + 15 - 14 +"))
print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))