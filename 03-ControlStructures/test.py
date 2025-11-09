# 1.3
# # Checking whether a car exceeded the speed limit
# #
# speed_limit = 140
# car_speed = int( input('Enter car speed (km/h): ') )

# if car_speed > speed_limit:
#     print(f'Your speed is {car_speed}km/h')
#     print('Warning: speed limit exceeded!!')
# else:
#     print("car speed is fine")

# ------------------------------------------------------------- #

# 1.4

# ###
# # Credit card payment 
# #
# account_balance = 500
# total_payment = int(input("enter value "))

# if total_payment < account_balance:
#     print('Payment completed')
# else:
#     print('No funds')

# ------------------------------------------------------------- #

# 1.5

# ###
# # Checking whether the test is passed
# # Test is passed when the number of correctly completed
# # tasks is at least 50%
# #
# total_tasks = 20
# tasks_ok = int(input("wprowadz ilosc poprawnych zadan "))
# test_passed = False

# if tasks_ok >= (total_tasks * 0.5) :
#     test_passed = True

# if test_passed:
#     print('Congratulations! You passed the test.')
# else:
#     print('Unfortunately, you failed the test.')

# ------------------------------------------------------------- #

# # 1.6

# ###
# # Checking whether the number
# # entered from the keyboard is even or odd 
# #
# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')


# # 1.7

# ------------------------------------------------------------- #

# ###
# # Program that calculates the employee's salary,
# # taking into account the possibility of receiving a bonus.
# #
# basic_salary = 5000
# total_salary = 0
# bonus = 0.15 # 15%
# is_bonus = str(input('Does the employee receive a bonus? (Y/N):') )

# if is_bonus == "Y":
#     total_salary = (basic_salary*bonus + basic_salary)
# else:
#     total_salary = basic_salary

# print(f'Basic salary: {basic_salary}')
# print(f'Bonus included? {is_bonus}')
# print(f'Total salary: {total_salary}')

# ------------------------------------------------------------- #

# # 2.1

# x = int(input("Podaj liczbe "))
# if x > 3 and x < 10:
#     print(f"liczba x rowna sie {x} i jest poprawna")
# elif x % 2 == 0:
#     print(f"liczba {x} jest parzysta")
# elif x == 25:
#     print(f"liczba rowna sie dokladnie {x} ")
# else:
#     print(f"liczba jest dziwna")



# ------------------------------------------------------------- #

# # 2.2
# ###

# # A program for checking clothing sizes
# # S: Small size, M: Medium size, L: Large size
# # XL: Extra large size or Incorrect symbol (if entered symbol
# # dirrerent than S, M, L, XL)
# #
# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print('M: Medium size')
# elif size =='L':
#     print('L: Large size')
# elif size == 'XL':
#     print("XL: Extra large")

# else:
#     print("Wrong names")

# ------------------------------------------------------------- #

# 2.3

# ###
# # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# # In each of these three modes, the average fuel consumption in liters
# # per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# # total fuel consumption for a given distance in km and a given
# # driving mode.
# #
# driving_mode = input('Enter driving mode (A/M/E): ')
# distance = int(input('Enter distance in km '))

# if driving_mode == 'A':
#     fuel_consumption = 7 # liters per 100km
# elif driving_mode == 'M':
#     fuel_consumption = 9 #liters per 100km
# elif driving_mode == 'E':
#     fuel_consumption = 6 # liters per 100km
# else : 
#     print("nie wiem")

# total_consumption = (fuel_consumption * distance)/100
# print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')



# ------------------------------------------------------------- #


# # 2.4
# ###
# # Simple calculator
# # Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# # and two numbers. The program should perform the appropriate
# # mathematical operation on the given numbers and return the result.   
# # 
# number1 = int(input("Wprowadz pierwszą liczbę: "))
# number2 = int(input("Wprowadz drugą liczbę: "))
# operator = input("Wprowadz znak operacji, którą chcsz wykonać: ")

# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2
# elif operator == '*':
#     result = number1 * number2
# elif operator == '/':
#     result = number1 / number2

# # print result
# print(f'{number1} {operator} {number2} = {result}')



# ------------------------------------------------------------- #


# # 2.5
# ###
# # Calculates and prints the quarter of the year for a given
# # month number (1..12)
# #
# month = int(input('Enter month number (1..12): '))

# if month >= 10:
#     quarter = 4
# elif month >=6:
#     quarter = 3
# elif month >=3:
#     quarter = 2
# else:
#     quarter = 1

# print(f'Month {month} is in quarter {quarter}')



# ------------------------------------------------------------- #




# # 2.6

# # Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:

# # 7, 1 ,0 ,-1 , -4

# wprowadzonaWartosc = int(input("Enter the number: "))
# if wprowadzonaWartosc > 0:
#     print(f' Number {wprowadzonaWartosc} is positive')
# elif wprowadzonaWartosc < 0:
#     print(f'Number {wprowadzonaWartosc}  is negative')
# else:
#     print(f'Number {wprowadzonaWartosc}  is 0')


# ------------------------------------------------------------- #






# 3  ----------------------- 3 #


# # 3.2

# ###
# # Checking login and password
# #
# login = 'joe'
# password = 'abcd'
# entered_login = input('Login: ')
# entered_password = input('Password: ')
# if login == entered_login and password == entered_password:
#     print('You are logged in')
# else:
#     print('Incorrect login or password!!')

# ------------------------------------------------------------- #

# 3.3

# ###
# # Checking if discount is available
# # The discount is available to children under 18,
# # or people 65 or older.
# #
# age = int(input('Enter your age: '))

# if age in range (1,18) or age in range (65,125) :
#     print("Discount is available")
# else:
#     print("Discount is not available")


# ------------------------------------------------------------- #

# # 3.4

# ###
# # Checks whether at least one number entered
# # from the keyboard is not negative
# # 
# x = int(input('Enter first number: '))
# y = int(input('Enter second number: '))

# if not x < 0 or y > 0  :
#     print(f'At least one of the numbers {x} and {y} is not negative')
# else:
#     print("both of numbers are negative")


# ------------------------------------------------------------- #

# # 3.5

# ###
# # Calculates the number of days in a month
# #
# month = int(input('Enter month number (1..12)'))

# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
#     days = 31 ## months with 31 days
# elif month==4 or month==6 or month==9 or month==11:
#     days = 30 ## months with 30 days
# else :
#     days = 28
# ## February 28 days 

# print(f'Month {month} has {days} days')


# ------------------------------------------------------------- #

# # 3.6

# ###
# # Checks if the given day number of the month is correct
# #
# month = int(input('Enter month number (1..12): '))
# day = int(input('Enter the day number of the month: '))
# day_ok = False

# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
#     if day >=1 and day <= 31:
#         day_ok = True
# elif  month==4 or month==6 or month==9 or month==11:
#     if day >=1 and day <= 30:
#         day_ok = True
# elif month ==2:
#     if day >= 1 and day <= 28:
#         day_ok = True
# else:
#     print("that month doesnt exist")
    

# message = f'Day {day} for the month {month}'
# if day_ok:
#     print(f'{message} is correct')
# else:
#     print(f'{message} is incorrect')





# ------------------------------------------------------------- #


# 4.1


# for i in range(4):
#     print('Practice makes perfect!')



# 4.4


###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '
    
    
    
print(university)
print(university_expanded)

# print(university) # original university name
# print(university_expanded) # expanded university name








