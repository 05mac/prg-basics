matrix = ([1, 2, 3],
   [4, 5, 6],
   [7, 8, 9])


# Główna: 1 + 5 + 9 = 15
# Przeciwna: 3 + 5 + 7 = 15
# --> True

matrix2 = ([10, 2, 3],
   [4, 5, 6],
   [7, 8, 1])
# Główna: 10 + 5 + 1 = 16
# Przeciwna: 3 + 5 + 7 = 15
# --> False

n = len(matrix2)

suma = 0
for i in range(n):
    if matrix2[i][i]:
        suma += matrix2[i][i]
print(suma)

# glowna_przekatna = [matrix2[i][i] for i in range(n)]
# suma_glowna = sum(glowna_przekatna)
# print(suma_glowna)
        