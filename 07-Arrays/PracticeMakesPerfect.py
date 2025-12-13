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
my_tuple = (50,20,40,50,30,50)

liczba = int(input("Podaj liczbe: "))
counter = 0

for i in my_tuple:
    if i == liczba:
        counter += 1
print(f"Number of occurrences: {counter}")


