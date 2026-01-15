###
# Calculates arithmetic mean of two integer numbers
#

# /////////////////////////////////////////////////////


# 1. 


# def mean(x, y):
#     wynik = (x + y)/2
#     return wynik


# # takes two numbers from keyboard
# n1 = int(input("Podaj jedną liczbę: "))
# n2 = int(input("Podaj drugą liczbę: "))

# # calculates arightmtic mean and print result
# result = mean(n1, n2)
# print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')


# /////////////////////////////////////////////////////

# 2.

# # takes two numbers from keyboard
# n1 = int(input("podaj pierwsza liczbę: "))
# n2 = int(input("podaj drugą liczbę: "))


# # define an anonymous function
# mean = lambda x,y: (x+y)/2


# # calculates arightmtic mean and print result
# result = mean(n1,n2)
# print(f"The arithmetic mean of {n1} and {n2} is {result}")


# /////////////////////////////////////////////////////


# # 3.

# def ms_to_kmh(ms):
#     kmh = ms * 3.6

#     return f"{kmh} km/h"


# predkosc = ms_to_kmh(10)
# predkosc2 = ms_to_kmh(35)

# print(predkosc, predkosc2)



# /////////////////////////////////////////////////////



# #4.

# ms_to_kmh = lambda predkosc: predkosc * 3.6
# print(f"{ms_to_kmh(10)} km/h")
# print(f"{ms_to_kmh(35)} km/h")


# /////////////////////////////////////////////////////

# # 6.  

# distance = float(input("Podaj dystans w kilometrach: "))
# hours = int(input("Podaj godziny jazdy: "))
# minutes = int(input("Podaj minuty jazdy: "))

# avg_speed = lambda distance,hours,minutes: (distance / ((hours * 60) + minutes)) * 60 

# print(f"{avg_speed(distance,hours,minutes):.1f} km/h")



# /////////////////////////////////////////////////////

# # # 7.  

# is_even = lambda x: x % 2 == 0

# print(is_even(3))
# print(is_even(2))

# /////////////////////////////////////////////////////

# # # # 8. 


# initials = lambda name, surname: name[0] + surname[0]

# print(initials("Motor","Michał"))





# 2222222222222222222222222222222
# /////////////////////////////////////////////////////


# def min_pts(limit):
#    def check(pts):
#       if pts >= limit:
#          return True
#       return False
#    return check

# print("=== MIN 50 PTS TO PASS ===")
# assess_test = min_pts(50)
# print(f"52 pts -> {assess_test(52)}")
# print(f"39 pts -> {assess_test(39)}")

# print("=== MIN 60 PTS TO PASS ===")
# assess_test = min_pts(60)
# print(f"52 pts -> {assess_test(52)}")
# print(f"39 pts -> {assess_test(39)}")


# /////////////////////////////////////////////////////

# # 2.2

# #Unsorted list:
# names = [
#    'James',
#    'Emily',
#    'William',
#    'Olivia',
#    'Benjamin',
#    'Sophia',
#    'Henry']

# print(sorted(names,key= lambda lista: len(lista)))

# /////////////////////////////////////////////////////

### 3.   


#3.1

# transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
# transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
# print(transactions_in_pln)

# /////////////////////////////////////////////////////


# #3.2

# sentence = 'I completely agree with you'
# result = list(map(lambda text: len(text) , sentence.split()))
# print(f"No. of letters in words: {result}")


# # 3.3

# stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

# result = sum(map(lambda x : x[0] * x[1], stock ))
# print(f"Total value: {(result)}")


# # dodatkowe zadanie 1

# prices_netto = [100, 250, 40, 60, 120]

# prices_brutto = list(map(lambda x: x * 1.23, prices_netto))
# formatted_prices = list(map(lambda x:(f"Cena: {x:.2f} PLN"), prices_brutto ))
# print(prices_brutto)
# print(formatted_prices)




# # # dodatkowe zadanie 2

# data = [("Anna", 50), ("Robert", 75), ("Kasia", 40)]

# tresc = list(map(lambda x:       f"{x[0]}: Zdał" if x[1] >= 50       else f"{x[0]}: Nie zdał ", data))
# print(tresc)



# /////////////////////////////////////////////////////


# rozdzial 4 

# # 1.
# employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
#                "JACKSON Peter","JOHNSON Rick",
#                "LEWIS Terry","CLARKE Robin"]
# emp_J = list(filter(lambda e: e[0]=="J", employees))
# pracownik = "\n".join(emp_J)
# print(pracownik)

# /////////////////////////////////////////////////////

#2. 

# predkosci = [48,47,54,50,42,68,39,46]

# fotoradar = list(filter(lambda x: x > 50,predkosci))
# print(fotoradar)


#3. 

# /////////////////////////////////////////////////////

# final_grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2.0]

# arithmetic_mean = list(filter(lambda x: x != 2 , final_grades))
# result = (sum(arithmetic_mean)/ len(arithmetic_mean))  
# print(f"{result:.2f}")


# /////////////////////////////////////////////////////

# 5. Data Reducing

from functools import reduce

# Function to add two numbers
def add(x, y):
   return x + y

numbers = [2,4,6,3,7,5]

parzysta_lista = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Liczby parzyste to: {parzysta_lista}")

suma_parzystych = (reduce(add, parzysta_lista))
print(f"Suma parzystych to: {suma_parzystych}")
