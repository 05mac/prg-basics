##########              PRACTICE MAKES PERFECT               ##########

# 1.

# array = [34,7,19,4,21,8]


# i = 0
# n = len(array)
# counter = 0
# while i < n:
#     if array[i] % 2 == 0:
#         counter += array[i]
#     i += 1
# print(counter)


##########              PRACTICE MAKES PERFECT               ##########


# 2.


# array = [15, 8, 31, 47, 2, 19]

# print("existed array:", end=" ")

# for i in array:
#     print(i, end=" ")

# print()
# print("revers array: ", end=" ")
# for i in reversed(array):
#     print(i, end=" ")


##########              PRACTICE MAKES PERFECT               ##########


# 3.

# array = [8,2,5,1,9]

# print("existed array:", end=" ")
# for i in array:
#     print(i, end=" ")

# print()

# print("2nd power:", end=" ")
# for i in array:
#     print(f"{i*i}", end=" ")


##########              PRACTICE MAKES PERFECT               ##########


# 4.


# -------------------  METODA Z SORTOWANIEM BABELKOWYM

# array = [-15, 8, -31, 47, -2, 19]

# n = len(array)

# def swap (array,dx1,dx2):
#     array[dx1], array[dx2] = array[dx2], array[dx1]

# for i in range (n-1):
#     for j in range(n-i-1):
#         if array[j] < array[j +1]:
#             swap(array,j,j+1)

# print (f"Maxium: {array[0]}")
# print (f"Minimum: {array[5]}")

# ----------------------------------------------------

# DRUGI SPOSOB BEZ SORTOWANIA BABELKOWEGO !
# #
# array = [-15, 8, -31, 47, -2, 19]

# current_min = array[0]
# current_max = array[0]

# for element in array[1:]:

#     if element > current_max:
#         current_max = element

#     if element < current_min:
#         current_min = element

# print(f"Maximum: {current_max}")
# print(f"Minimum: {current_min}")

##########              PRACTICE MAKES PERFECT               ##########


# 5.

# array = [15, 8, 31, 47, 2, 19]

# counter = len(array)
# sum = 0
# for i in array:
#     sum += i
#     print(i, end=" ")

# print()
# print(f"suma elementow tablicy wynosi: {sum}")
# print(f"Średnia arytmetyczna elemntow tablicy wynosi: {sum/counter:.2f}")


##########              PRACTICE MAKES PERFECT               ##########

# 6.

# array = [15, 8, 31, 47, 2, 19]

# n = len(array)
# i = 0
# sum = 0
# while i < n:
#     sum += array[i]
#     i += 1

# print(f"suma elementow tablicy wynosi: {sum}")
# print(f"srednia arytmetyczna elementow tablicy wynosi: {sum/n:.2f}")


##########              PRACTICE MAKES PERFECT               ##########


# 7.

# array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# longest_name = max(array, key=len)
# print(array)
# print(f"Longest name: {longest_name}")


##########              PRACTICE MAKES PERFECT               ##########


# 8.

# array = [2,6,4,9,7]

# def star(n):
#     return ("*" * n)

# for value in array:
#     asterisks = star(value)
#     print(f"{value}: {asterisks}")


##########              PRACTICE MAKES PERFECT               ##########

# 9.

# def compare(array1, array2):
#     if len(array1) != len(array2):
#         return False

#     n = len(array1)
#     for i in range(n):
#         if array1[i] != array2[i]:
#             return False
#     return True

# print(compare(["water","book","sky"],["water","book","sky"]))
# print(compare([True,False],[True,False,True]))
# print(compare([5,3,1],[5,3,1]))
# print(compare([3,2,1],[3,2]))


##########              PRACTICE MAKES PERFECT               ##########

# 10.

# array1 = [4,36,12,28,9,44,5]
# array2 = [5,1,36]

# for element in array1:
#     if element in array2:
#         continue
#     else:
#         print(element, end=" ")

##########              PRACTICE MAKES PERFECT               ##########

# 11.

# def bubble_sort(array):

#     def swap(array, dx1, dx2):
#         array[dx1], array[dx2] = array[dx2], array[dx1]

#     n = len(array)

#     for i in range(n-1):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 swap(array,j,j+1)
#         return array


# print(bubble_sort([1,5,2,2,3,8,6,7]))


##########              PRACTICE MAKES PERFECT               ##########

# 12.

# array = [2,3,2,5,8,1,9,8]
# unique_array = []

# print("Array:")
# for i in array:
#     print(i, end=" ")


# print()

# for element in array:
#     if array.count(element) == 1:
#         unique_array.append(element)

# print(f"Unique elements: {unique_array}")

##########              PRACTICE MAKES PERFECT               ##########

# 13.

# def occurs (number,array):
#     if number in array:
#         return True
#     else:
#         return False

# print(occurs(23,[15,38,7,23,14]))


##########              PRACTICE MAKES PERFECT               ##########

# 14.

# def f():
#     my_tuple = ("computation", )

#     return type(my_tuple)


# print(f())


##########              PRACTICE MAKES PERFECT               ##########

# # 15.

# my_tuple = (10,20,30,40,50)

# print(tuple(reversed(my_tuple)))


##########              PRACTICE MAKES PERFECT               ##########

# # 16.
# my_tuple = ("Seven", [10,20,30],(5,15,25))

# print(my_tuple[0],my_tuple[1][2])


##########              PRACTICE MAKES PERFECT               ##########

# 17.
# my_tuple = (50,20,40,50,30,50)

# liczba = int(input("Podaj liczbe: "))
# counter = 0

# for i in my_tuple:
#     if i == liczba:
#         counter += 1
# print(f"Number of occurrences: {counter}")


##########              PRACTICE MAKES PERFECT               ##########


# import math
# # 18.


# def MyArrays(array):

#     def swap(array, dx1, dx2):
#         array[dx1], array[dx2] = array[dx2], array[dx1]

#     n = len(array)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 swap(array, j, j+1)

#     druga_naj = array[-2]
#     roznica = array[-1] - array[0]

#     if n % 2 == 0:
#         mediana = int(n / 2)
#         wynik_mediany = (array[mediana-1] + array[mediana]) / 2
#     else:
#         mediana = (n // 2)
#         wynik_mediany = array[mediana]

#     print(array)
#     print(druga_naj)
#     print(wynik_mediany)
#     print(array[0],array[-1])


# if __name__ == "__main__":
#     array = [7, 3, 8, 5, 2]
# print(MyArrays(array))


##########              PRACTICE MAKES PERFECT               ##########

# # 19.

# liczba = float(input("Podaj liczbe: "))
# array = [-2,-1,2,5,6]

# licznik = 0
# for element in array:
#     if liczba < element:
#         licznik += 1
# print(licznik)


##########              PRACTICE MAKES PERFECT               ##########


# 20.

# arr = [2,3,4,5,6,7,8,9,10,12,13,13,25]
# licznik = 0
# for index,value in enumerate(arr):
#     if value % 2 == 0:
#         arr[index],arr[licznik] = arr[licznik],arr[index]
#         licznik += 1
# print (arr)


##########              PRACTICE MAKES PERFECT               ##########

#  # 21.

# arr2 = [1,2,3,4,5,6]
# arr1 = [1,2,3]

# set1 = set(arr1)
# set2 = set(arr2)


# z = set1.issubset(set2)
# print(z)


##########              PRACTICE MAKES PERFECT               ##########


# # 22.
# import random
# def rand_elem(array):
#     n = len(array)
#     losowa_liczba = random.randrange(n)
#     return(array[losowa_liczba])
# print((rand_elem([2,1,3,2,4,5])))

##########              PRACTICE MAKES PERFECT               ##########


# 23.

# t = "An apple a day keeps the doctor away"

# def MyText(t):
#     words = t.split()
#     number_Words = len(words)
#     LongToShort = sorted(words, key=len)
#     alphabetically = sorted(words, key=str.lower)


##########              PRACTICE MAKES PERFECT               ##########

# 28.


# arr = [
#         [7,3,7,9,0],
#         [2,9,0,1,5],
#         [3,8,6,4,7],
#         [8,7,1,1,5]
#        ]

# # kolumna = [sum(kolumna) for kolumna in zip(*arr)]
# # print(kolumna[4])

# suma_kolumny = 0
# for i in arr:
#     suma_kolumny += i[4]

# print(suma_kolumny)

##########              PRACTICE MAKES PERFECT               ##########

# 29.

# def create_2d_arr(x,y):
#     tablica = []

#     for i in range(x):
#         dodatkowa_tablica = []
#         for j in range(y):
#             dodatkowa_tablica.append(0)

#         tablica.append(dodatkowa_tablica)

#     return tablica


# print(create_2d_arr(3,5))


##########              PRACTICE MAKES PERFECT               ##########


# 30.

# array = [[0, 0, 0, 0, 0], # 1
#          [0, 0, 0, 0, 0], # 2
#          [0, 0, 0, 0, 0], # 3
#          [0, 0, 0, 0, 0], # 4
#          [0, 0, 0, 0, 0]] # 5

# n = len(array)

# for i in range(n):
#     for j in range(n):
#         array[i][j] = (j + 1)* (i+1)

# for element in array:
#     print(element)


##########              PRACTICE MAKES PERFECT               ##########

# 31.

# array = [   [-38, 19],
#             [5,40],
#             [-7,11],
#             [29,16]
#             ]

# n = len(array)
# najwieksza = array[0][0]
# najmniejsza = array[0][0]

# row_max, col_max = 0,0
# row_min, col_min = 0,0

# for indexWiersz, valueWiersz in enumerate(array):
#     for indexKolumna, valueKolumna in enumerate(valueWiersz):
#         if valueKolumna > najwieksza:
#             najwieksza = valueKolumna
#             row_max = indexWiersz
#             col_max = indexKolumna

#         if valueKolumna < najmniejsza:
#             najmniejsza = valueKolumna
#             row_min = indexWiersz
#             col_min = indexKolumna


# print(f"najwieksza wartosc to: {najwieksza} oraz ma indeks {row_max,col_max}")
# print(f"Natomiast wartosc najmniejsza to {najmniejsza} oraz ma indeks {row_min, col_min}")


##########              PRACTICE MAKES PERFECT               ##########


# for row in array:
#     for column in row:
#         if column > najwieksza:
#             najwieksza = column

#         if column < najmniejsza:
#             najmniejsza = column


# print(najwieksza,",",najmniejsza)


##########              PRACTICE MAKES PERFECT               ##########

# 32.

# array = [
#     [6, 6, 6, 6, 6],
#     [5, 5, 5, 5, 5],
#     [4, 4, 4, 4, 4],
# ]
# n = len(array)
# # print(f"Przed zamiana ")
# print(f"Matirx przed zmiana: {array}")
# array[0],array[-1] = array[-1],array[0]

# print(f"Matrix po zmianie: {array}")


##########              PRACTICE MAKES PERFECT               ##########


# 33.

# array = [
#     [3, 6, 6, 6, 7],
#     [2, 5, 5, 5, 7],
#     [1, 4, 4, 4, 7],
# ]


# n = len(array)

# counter = 0
# for i in range(n):
#     array[i][-1],array[i][0] = array[i][0],array[i][-1]
# print(array)

# for element in array:
#     print(element)


##########              PRACTICE MAKES PERFECT               ##########


# # 34.

# def identity_matrix(n):

#     tablica = []
#     for i in range(n):
#         tablica_pomocnicza = []
#         for j in range(n):
#             if i == j:
#                 tablica_pomocnicza.append(1)
#             else:
#                 tablica_pomocnicza.append(0)
#         tablica.append(tablica_pomocnicza)


#     return tablica


# for element in (identity_matrix(5)):
#     print(element)


##########              PRACTICE MAKES PERFECT               ##########

# # 35. Transpose Matrix

# def transpose_matrix(matrix):
#     n_rows = len(matrix)
#     n_cols = len(matrix[0]) # Szybki sposób na kolumny
    
#     czysta_tablica = []
    
#     # Pętla po kolumnach oryginału (staną się wierszami)
#     for i in range(n_cols):
#         pomocnicza_tablica = []
#         # Pętla po wierszach oryginału (staną się kolumnami)
#         for j in range(n_rows):
#             # Twoja świetna logika indeksów j, i
#             pomocnicza_tablica.append(matrix[j][i]) 
#         czysta_tablica.append(pomocnicza_tablica)
        
#     return czysta_tablica

# # Testy
# array1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
# array2 = [[5, 6, 7, 8]]

# def print_2d(matrix):
#     for row in matrix:
#         print(" ".join(map(str, row)))

# print("Macierz 1 transponowana:")
# res1 = transpose_matrix(array1)
# print_2d(res1)

# print("\nMacierz 2 transponowana:")
# res2 = transpose_matrix(array2)
# print_2d(res2)




##########              PRACTICE MAKES PERFECT               ##########


# 36. 

# array = [[5,0,3,7,5],[9,0,9,1,2]]
array = [[2,1],[3,5],[7,4],[2,6]]

nowa_tablica = []

for wiersz in array:
    nowa_tablica.extend(wiersz)
    
print(f"Stara tablica {array}")
print(f"Nowa tablica {nowa_tablica}")