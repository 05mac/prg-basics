array = [[-38, 19], [5,40],[-7,11],[29,16]]
# min = 0
# max = 0
for row in array:
    for element in row:
       data = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# 1. Inicjalizacja: Zakładamy, że pierwszy element jest i najmniejszy, i największy
min_val = data[0][0]
min_pos = (0, 0) # Przechowujemy krotkę (wiersz, kolumna)

max_val = data[0][0]
max_pos = (0, 0)

# 2. Pętla po wierszach (indeks r)
for r in range(len(data)):
    # 3. Pętla po kolumnach (indeks c)
    for c in range(len(data[r])):
        current_val = data[r][c]
        
        # Sprawdzamy czy znaleźliśmy nowe minimum
        if current_val < min_val:
            min_val = current_val
            min_pos = (r, c)
            
        # Sprawdzamy czy znaleźliśmy nowe maksimum
        if current_val > max_val:
            max_val = current_val
            max_pos = (r, c)

# 4. Wyniki
print(f"Smallest value: {min_val} located at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest value: {max_val} located at row {max_pos[0]}, column {max_pos[1]}")