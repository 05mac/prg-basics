# Write a program that converts a decimal number into a binary number.

decimal_number = int(input("Enter decimal number: "))

# Zapamiętujemy oryginalną liczbę do wyświetlenia na końcu,
# bo 'decimal_number' w pętli zniszczymy (zdzielimy do zera).
original_number = decimal_number

binary_result = ""

# Obsługa zera (bo pętla while > 0 by go nie obsłużyła)
if decimal_number == 0:
    binary_result = "0"
else:
    # Dopóki liczba jest większa od 0
    while decimal_number > 0:
        remainder = decimal_number % 2       # 1. Oblicz resztę
        decimal_number = decimal_number // 2 # 2. Podziel liczbę
        
        # Dodajemy resztę do wyniku (jako napis)
        binary_result += str(remainder)

# ODWRACANIE:
# W Pythonie najłatwiej odwrócić napis używając [::-1]
# To oznacza: "weź cały napis, ale idź od tyłu krokami po -1"
binary_result = binary_result[::-1]

# Wyświetlanie w wymaganym formacie
print(f"{original_number}(10) = {binary_result}(2)")