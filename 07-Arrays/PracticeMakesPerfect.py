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
 
#----------------------------------------------------

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



