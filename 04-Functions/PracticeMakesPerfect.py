
# Practice Makes Perfect

# # 3.
# def month(n):
#     months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

#     if 1 <= n <= 12:
#             # Zwracamy element z listy. Odejmujemy 1, bo w informatyce liczymy od zera.
#             return months[n-1]
#     else:
#             return "Niepoprawny numer miesiąca"


# if __name__ == "__main__":
#     n = int(input("podaj numer miesiaca: "))
#     print(f"The name of month {n} is {month(n)}")


# 4.

# def liczenieLiter(litera,tekst):
#     licznik = 0
#     for i in tekst:
#         if i == litera:
#             licznik += 1
#     return licznik


# wynik = (liczenieLiter("e","You never get a second chance to make a first impression"))

# print(f"The number of letter 'e': {wynik}")

# 5.

# def isInRange(number,x,y):
#     if number in range(x,y+1):
#         return True
#     else:
#         return False

# print(isInRange(15,8,15))

# 6.

# def hide(card_number):

#     hide_number = ""

#     for indeks, cyfra in enumerate(card_number):
#         if indeks in range(0, 2) or indeks in  range(12, 16):
#             hide_number += cyfra
#         else:
#             hide_number +=  "*"
#     return hide_number


# print(hide("5290312400019022"))



# 6 - sposob ze slicingiem!!!!

def hide(card_number):
       
    return card_number[-2:] + "*" * 10 + card_number[-4:]

if __name__ == "__main__":
    print(hide("5290312400019022"))

# 7.

# def f(binary_number):

#     for cyfra in binary_number:
#         if cyfra != "0" and cyfra != "1":
#             return False

#     return True


# print(f("10100"))


# 8.

# def f (amount_to_pay):
#     licznikMonet = 0
#     while amount_to_pay >= 5:
#         amount_to_pay -= 5
#         licznikMonet += 1
#     while amount_to_pay >= 2:
#         amount_to_pay -= 2
#         licznikMonet += 1
#     while amount_to_pay >= 1:
#         amount_to_pay -=1
#         licznikMonet +=1
#     return licznikMonet

# print(f(80))


# def f (amount_to_pay):
#     licznikMonet = 0
#     while amount_to_pay >= 5:
#         amount_to_pay -= 5
#         licznikMonet += 1
#     while amount_to_pay >= 2:
#         amount_to_pay -= 2
#         licznikMonet += 1
#     while amount_to_pay >=1:
#         amount_to_pay -= 1
#         licznikMonet += 1
#     return licznikMonet


# print(f(2))

# 9

# def f (number, even):
#     licznikCyfr = 0
#     if even == True:
#         for i in str(number):
#             if int(i) % 2 == 0:
#                 licznikCyfr += int(i)

#     elif even == False:
#         for i in str(number):
#             if int(i) % 2 != 0:
#                 licznikCyfr += int(i)
#     return licznikCyfr


# print(f(3124,True))
# print(f(3124,False))
# print(f(20576,False))
# print(f(20576,True))
# print(f(13115,True))


# 10

# def f (x,y):
#     licznik = 0
#     for i in range(x,y):
#         if i < 0 and i % 2 == 0:
#             licznik += 1
#     return licznik


# print(f(-7,8))
# print(f(-1,11))


# 11

# def f (n1,n2,n3):
#     if n1 > 0 and n2 > 0 and n3 > 0:
#         return False
#     else:
#         return True

# print(f(5,4,14))
# print(f(11,6,-4))
# print(f(-5,-2,0))


# 12.

# def f(n):
#     napis = ""
#     i = 0
#     if n <= 0:
#         return "nie moze byc 0 lub ujemna!"
#     elif n == 1:
#         return "*"
#     else:
#         while i < n:
#             napis += "*/"
#             i += 1
#             if i ==n:
#                 napis += "*"
#         return napis


# print(f(10))
# print(f(0))

# 13.

# def f (n):
#     i = 1
#     napis = ""
#     while i <=n:
#         napis += str(i)
#         i += 1
#     return str(napis)

# print(f(11))
# print(f(4))

# 14.

# def f(number1,number2,operator):
#     if operator == "+":
#         return number1 + number2
#     elif operator == "%":
#         return number1 % number2
#     elif operator == "**":
#         return number1 ** number2
#     elif operator == "*":
#         return number1 * number2
#     elif operator == "-":
#         return number1 - number2

# print(f(2,3,"+"))
# print(f(2,3,"%"))
# print(f(2,3,"**"))
# print(f(2,3,"*"))
# print(f(2,3,"-"))


# 15.

# def f(detector):
#     licznikOsob = 0
#     for i in detector:
#         if i == "+":
#             licznikOsob += 1
#             if licznikOsob == 3:
#                 return True
#         elif i == "-" and licznikOsob > 0:
#             licznikOsob -= 1
#             if licznikOsob == 3:
#                 return True
#     return False


# print(f("+-+++-+---"))
# print(f("+-+-+-+-"))
# print(f("+-++-+--"))
# print(f("+-++-++-+---"))


# 16.

#########