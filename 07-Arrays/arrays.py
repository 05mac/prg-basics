# # 2.2
# # 3x3 Tic-Tac-Toe board
# tic_tac_toe_board = [
#    ['X', 'O', 'X'],
#    [' ', 'X', 'O'],
#    ['O', ' ', 'X']
# ]

# for row in tic_tac_toe_board:
#    for item in row:
#       print(item, end=" ")
#    print()


# # 2.3

# # Weekly expenses for different categories
# # [Food, Transport, Utilities]
# monthly_expenses = [
#    [200, 50, 100],  # Week 1
#    [180, 60, 110],  # Week 2
#    [220, 55, 105],  # Week 3
#    [210, 65, 95]    # Week 4
# ]


# food_total = 0
# transport_total = 0
# utilities_total = 0
# current_sum_week = 0
# grand_total = 0
# week_totals = []
# # Calculates expenses
# # Use loop statements
# for week in monthly_expenses:
#     food_total += week[0]
#     transport_total += week[1]
#     utilities_total += week[2]

#     #sumowanie tygodni, wierszy
#     current_sum_week = sum(week)
#     week_totals.append(current_sum_week)

#     grand_total += current_sum_week

# # Print expenses
# print('MONTHLY EXPENSES')
# print('----------------')
# print('Food:',food_total)
# print('Transport:',transport_total)
# print('Utilities:',utilities_total)
# print('Week 1:',week_totals[0])
# print('Week 2:',week_totals[1])
# print('Week 3:',week_totals[2])
# print('Week 4:',week_totals[3])
# print('---------------')
# print('TOTAL:',grand_total)


# ----------------------------------------------- #


# # 4

# # Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
# meal_plan = [
#     ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
#     ["Pancakes", "Sandwich", "Steak"],
#     ["Smoothie", "Chicken Wrap", "Salmon"],
#     ["Eggs", "Pasta", "Soup"],
#     ["Toast", "Burrito", "Pizza"],
#     ["Cereal", "Salad", "Fish Tacos"],
#     ["Bagel", "Rice and Beans", "Stir-fry"]
# ]

# # Returns a week day name
# def weekday(n):
#     weekdays = ["Monday", "Tuesday", "Wednesday",
#                 "Thursday", "Friday", "Saturday", "Sunday"]
#     return weekdays[n-1]

# # Returns a string with day meal names
# # separated by comma


# def day_meal_plan(meal_plan, day_number):
#   # Pobieramy listę posiłków dla danego dnia (np. ["Eggs", "Pasta", "Soup"])
#    daily_meals = meal_plan[day_number-1]

#    # Łączymy elementy listy w jeden tekst, rozdzielając je przecinkiem i spacją
#    return ", ".join(daily_meals)


# # Prints weekly meal plan
# print("WEEKLY MEAL PLAN")
# print("(Breakfast, Lunch, Dinner)")

# i = 1
# while i <= 7:
#     print(weekday(i) + ": " +  day_meal_plan(meal_plan,i))
#     i += 1


# ----------------------------------------------- #

# # 5

# # 5x5 cinema seating
# # A = Available, B = Booked
# cinema_seats = [
#     ['A', 'A', 'B', 'A', 'A'],
#     ['A', 'B', 'B', 'A', 'A'],
#     ['A', 'A', 'A', 'A', 'B'],
#     ['B', 'A', 'A', 'A', 'A'],
#     ['A', 'B', 'A', 'A', 'A']
# ]


# def seats_total(seats):
#     counter_all = 0
#     for row in seats:
#         for i in row:
#             counter_all += 1
#     return counter_all


# def seats_available(seats):
#     counter_a = 0
#     for row in seats:
#         for i in row:
#             if i == "A":
#                 counter_a += 1
#     return counter_a


# def seats_booked(seats):
#     counter_b = 0
#     for row in seats:
#         for i in row:
#             if i == "B":
#                 counter_b += 1
#     return counter_b


# def seat_status(seats, row, place):
#     if seats[row-1][place-1] == "A":
#         return "available"
#     else:
#         return "booked"


# print('CINEMA INFORMATION TABLE')
# print('Total seats:', seats_total(cinema_seats))
# print('Seats available:', seats_available(cinema_seats))
# print('Seats booked:', seats_booked(cinema_seats))
# print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
# print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
# print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))


# ----------------------------------------------- #


# 6

# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# for i in range(len(matrix)):
#     matrix[i][i] = 1


# extra 6 --------- drugi sposob

# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# # Użyj pętli i range(), tak jak poprzednio
# for i in range(len(matrix)):
#     if i == 0:
#         matrix[i][2] = 1
#     if i == 1:
#         matrix[i][1] = 1
#     if i == 2:
#         matrix[i][0] = 1


# # Wypisanie wyniku
# for row in matrix:
#     print(row)


# matrix2 = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# n = len(matrix2) # Rozmiar macierzy (3)

# for i in range(n):
#     # n - 1 to ostatni indeks (2)
#     # odejmujemy 'i', żeby cofać się o jeden w każdym kroku
#     matrix2[i][n - 1 - i] = 1

# print(matrix2)


# 3. Practice makes perfect

numbers = [34,7,19,4,21,8]

suma = 0
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        suma += numbers[i]
    i += 1

print(suma)