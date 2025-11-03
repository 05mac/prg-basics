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
