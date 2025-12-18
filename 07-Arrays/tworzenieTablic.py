
# tablica = []

# for i in range(1,4):
#     wiersz = []
#     for j in range(1,4):
#         wiersz.append((i*j))
    
#     tablica.append(wiersz)

# print(tablica)


# n = len(tablica)

# suma = 0


# -------------------------------------------



# zliczanie glownej przkatnej
# for row in range(n):
#     suma +=(tablica[row][row])
# print(suma)

#zliczanie przeciwnej przkatnej

# for row in range(n):
#     suma += tablica[row][n-1]
#     n -=1
# print(suma)





# -------------------------------------------





# # Zacznij od pustej tablicy
# kino = [[0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0]]

# n = len(kino)

# for i in range(n):
#     for j in range(n):
#         kino[i][j] = ((i+1)  * 10) + (j + 1)

# for element in kino:
#     print(element)


# -------------------------------------------



# Zadanie: Stwórz tablicę 5x5 wypełnioną zerami i 
# jedynkami tak, aby tworzyły wzór szachownicy.

# tablica = []

# for i in range(5):
#     pomocnicza_tablica = []
#     for j in range(5):
#         liczba = j + i
#         if liczba % 2 == 0:
#             pomocnicza_tablica.append(0)
#         else:
#             pomocnicza_tablica.append(1)
#     tablica.append(pomocnicza_tablica)

# for element in tablica:
#     print(element)




# -------------------------------------------
# -------------------------------------------
# -------------------------------------------





# Zadanie 1: Licznik "Szczęśliwych Siódemek"Masz gotową tablicę $3 \times 3$. Napisz kod, 
# który policzy, ile razy występuje w niej liczba 7.



# tablica = [
#     [1, 7, 3],
#     [7, 5, 7],
#     [4, 8, 2]
# ]
# n = len(tablica)
# counter = 0
# for row in tablica:
#     for column in row:
#         if column == 7:
#             counter += 1
# print(counter)





# -------------------------------------------
# -------------------------------------------
# -------------------------------------------



# Zadanie 2: "Odwrócona Przekątna"Stwórz tablicę $4 \times 4$ wypełnioną zerami.
#  Następnie za pomocą pętli wypełnij jedynkami (1) 
# tylko drugą przekątną (tą od prawego górnego rogu do lewego dolnego)
# .Podpowiedź: Użyj zależności n - 1 - i, o której wczoraj rozmawialiśmy.


# tablica = []
# for i in range (4):
#     pomocniczna_tablica = []
#     for j in range(4):
#         pomocniczna_tablica.append(0)
#     tablica.append(pomocniczna_tablica)

# print(tablica)

# n = len(tablica)

# for i in range(n):
#     tablica[i][n-1-i] = 1

    
# for element in tablica:
#     print(element)




# -------------------------------------------
# -------------------------------------------
# -------------------------------------------



# Zadanie 3: Mini-Sudoku Checker
# Masz jeden wiersz z Twojego Sudoku (z obrazka): wiersz = [3, 4, 1, 2, 5, 6].
# Poproś użytkownika o podanie liczby i za pomocą enumerate wypisz,
# na którym indeksie (pozycji) znajduje się ta liczba w wierszu.

wiersz = [3, 4, 1, 2, 5, 6]
print(wiersz)
liczba = int(input("Podaj jakas liczbe z powyzszej listy: "))

for index,value in enumerate(wiersz):
    if value == liczba:
        print(f"twoja liczba: {liczba} znajduje sie na indeksie {index}")
       
