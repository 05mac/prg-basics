import math
# ###

# 2 --------------------------

# # Program for testing built-in functions
# #
# max_number = max(7,5,6,3,8,2)
# print('Max number of 7,5,6,3,8,2 is', max_number)

# min_number = min(4,7,2,3,9,8)
# print('Min number of 4,7,2,3,9,8 is', min_number)

# str_length = len("computer science")
# print('The number of characters in "computer science" is', str_length)

# letter_read = input("podaj litere: ")
# print("litera z klawiatury to: ", letter_read)

# number_represent = int("20303")
# print("numer reprezentuje: ",number_represent)

# binarystring = bin(304)
# print("Binary string represent is: ",binarystring)

# hexaString = hex(304)
# print("hexadecimal string decimal is: ", hexaString)

# integerRepre = ord("€")
# print("Unicode code of the € is: ",integerRepre)

# abso = abs(-17)
# print("absolute value of -17 is: ", abso)


# # 3 --------------------------

# 3.1

# ###
# # To use the functions available in an external module,
# # you must include that module in your program.
# import math

# square_root = math.sqrt(7)
# print('A square root of 7 is', square_root)

# natural_logarithm = math.log(5)
# print('A natural logarithm of 5 is: ', natural_logarithm)

# rad = math.radians(90)
# sine = math.sin(rad)
# print("sine of 90 degreees is: ", sine)


# # 3.2 

# ###
# # Generates and prints a random number between 1 and 6,
# # similar to rolling a dice
# #
# import random

# print(random.randint(1,6))



# # 4 --------------------------



# # 4.3

# # def function_name(parameters):
# #     # Code block (function body)
# #     return result  # Optional: Returns a value

# ###
# # Calculates the area of a triangle based on the lengths
# # of the triangle's sides
# #

# def triangle_area(a,b,c):
#     p = ((a+b+c)/2)
#     area = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     return area

# print(f'The area of ​​a triangle with sides 3, 4, 5 is {triangle_area(3,4,5)}')
# print(f'The area of ​​a triangle with sides 5, 12, 13 is {triangle_area(5,12,13)}')
# print(f'The area of ​​a triangle with sides 7, 24, 25 is {triangle_area(7,24,25)}')

# # 4.4


###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    if number < 0:
        abs(number)
    for char in number:
        
    

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')